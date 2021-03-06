from django.db import models
from user.models import User


class Survey(models.Model):
    name = models.CharField(max_length=300)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"


class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviews")
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviews_target")
    comment = models.TextField(default='', blank=True)
    created_at = models.DateField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="interviews")

    @property
    def is_done(self):
        count_questions = Question.objects.filter(survey_id=self.survey_id).count()
        count_grades = self.grades.all().count()
        return count_questions == count_grades

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Grade(models.Model):
    created_at = models.DateField(auto_now_add=True)
    value = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="grades")
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="grades")

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
        unique_together = ("interview_id", "question_id")