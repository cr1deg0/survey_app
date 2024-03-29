from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Survey(models.Model):
    """Model of a Survey. Default status at creation is DRAFT and slug is
    added automatically."""

    STATUS = [
        ("DRAFT", "Draft"),
        ("ACTIVE", "Publish"),
    ]
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="survey_author"
    )
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=6, choices=STATUS, default=STATUS[0][0])
    submissions = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("survey_edit", args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        permissions = (
            ("view_own_survey", "Can view own survey"),
            ("edit_own_survey", "Can edit own survey"),
            ("delete_own_survey", "Can delete own survey"),
        )


class Question(models.Model):
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="question_survey"
    )
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question

    class Meta:
        permissions = (
            ("view_own_question", "Can view own question"),
            ("edit_own_question", "Can edit own question"),
            ("delete_own_question", "Can delete own question"),
        )

    def get_absolute_url(self):
        return reverse("survey_edit", kwargs={"slug": self.survey.slug})


class Option(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="option_question"
    )
    option = models.CharField(max_length=250)
    selected = models.IntegerField(default=0)

    def __str__(self):
        return self.option

    def get_absolute_url(self):
        return reverse("survey_edit", kwargs={"slug": self.question.survey.slug})
