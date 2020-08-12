from rest_framework import serializers
from survey.models import Grade, Question, Category, Interview, Survey
from user.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(read_only=False)
    survey_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Question
        fields = ('id', 'description', 'category_id', 'survey_id', 'created_at', 'order')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'end_date', 'is_active')


class GradeSerializer(serializers.ModelSerializer):
    interview_id = serializers.IntegerField(read_only=False)
    question_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Grade
        fields = ('id', 'value', 'question_id', 'interview_id', 'created_at')


class SurveyQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'end_date', 'is_active', 'questions')


class InterviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=False)
    target_user_id = serializers.IntegerField(read_only=False)
    target_user = UserSerializer(many=False, read_only=True)
    survey_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'target_user', 'survey_id', 'created_at', 'comment', 'is_done')


class InterviewSurveyQuesitonSerializer(serializers.ModelSerializer):
    survey = SurveyQuestionsSerializer(read_only=True)
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'comment', 'survey', 'grades')
