from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name = models.CharField(max_length=300)


class Interview(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target_users")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="surveys")
    comment = models.TextField(default='')


class Category(models.Model):
    name = models.CharField(max_length=300)


class Question(models.Model):
    description = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="surveys")


class Grade(models.Model):
    created_at = models.DateField(auto_now_add=True)
    value = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions")
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="interviews")

