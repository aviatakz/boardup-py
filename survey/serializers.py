from rest_framework import serializers
from survey.models import Grade, Question, Category, Interview, Survey


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'description', 'category_id', 'survey_id', 'created_at')


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'value', 'question_id', 'interview_id', 'created_at')


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'survey_id', 'created_at', 'comment')
