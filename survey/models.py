from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField(default='')


class Interview(models.Model):
    created_at = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    target_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target_users")
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comments")


class Category(models.Model):
    name = models.CharField(max_length=300)


class Question(models.Model):
    description = models.TextField(default='')
    created_at = models.DateField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")


class Grade(models.Model):
    created_at = models.DateField()
    value = models.IntegerField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions")


class IntreviewGrade(models.Model):
    interview_id = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="interviews")
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="grades")

