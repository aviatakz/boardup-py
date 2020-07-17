from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"


class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target_users")
    comment = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="interviews")

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Question(models.Model):
    description = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Grade(models.Model):
    created_at = models.DateField(auto_now_add=True)
    value = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions")
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="grades")

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"