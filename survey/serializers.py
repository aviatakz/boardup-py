from rest_framework import serializers
from survey.models import Grade, Question, Category, Interview, Survey


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    survey_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Question
        fields = ('id', 'description', 'category_id', 'survey_id', 'created_at')


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'questions')


class GradeSerializer(serializers.ModelSerializer):
    interview_id = serializers.IntegerField(read_only=False)
    question_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Grade
        fields = ('id', 'value', 'question_id', 'interview_id', 'created_at')


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'survey_id', 'created_at', 'comment')


class InterviewSurveyQuesitonSerializer(serializers.ModelSerializer):
    survey = SurveySerializer(read_only=True)
    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'comment', 'survey')
