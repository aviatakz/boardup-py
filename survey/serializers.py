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


class QuestionGradeSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(many=False, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'description', 'category_id', 'survey_id', 'created_at', 'order', 'grade')


class SurveyQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionGradeSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'end_date', 'is_active', 'questions')


class InterviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=False)
    target_user_id = serializers.IntegerField(read_only=False)
    target_user = UserSerializer(many=False, read_only=True)
    survey_id = serializers.IntegerField(read_only=False)
    is_done = serializers.SerializerMethodField('check_is_done')

    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'target_user', 'survey_id', 'created_at', 'comment', 'is_done')

    def check_is_done(self, obj):
        has_ungraded = Question.objects.filter(survey_id=obj.survey_id, grade__isnull=True).exists()
        if has_ungraded:
            return False
        return True


class InterviewSurveyQuesitonSerializer(serializers.ModelSerializer):
    survey = SurveyQuestionsSerializer(read_only=True)

    class Meta:
        model = Interview
        fields = ('id', 'user_id', 'target_user_id', 'comment', 'survey')
