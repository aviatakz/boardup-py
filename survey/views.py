import json

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from survey.functions import average_list
from survey.models import Question, Interview, Grade, Survey, Category
from survey.serializers import QuestionSerializer, InterviewSerializer, \
    GradeSerializer, SurveySerializer, InterviewSurveyQuesitonSerializer, CategorySerializer, SurveyQuestionsSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['survey', 'category', ]

    @action(detail=False, methods=['post'])
    def create_questions(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterviewSurveyQuesitonSerializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def results(self, request):
        user_id = request.data["user_id"]
        survey_id = request.data["survey_id"]

        grades = Grade.objects.all()
        self_rating_grades = grades.filter(interview__survey=survey_id, interview__target_user=user_id,
                                           interview__user=user_id)
        self_res = average_list(self_rating_grades)
        colleagues_rating_grades = grades.filter(interview__survey=survey_id, interview__target_user=user_id).exclude(
            interview__user=user_id
        )
        colleagues_res = average_list(colleagues_rating_grades)
        company_res = average_list(grades)

        categories = {category.pk: category.name for category in Category.objects.all()}
        result_data = {"categories": categories, "self": self_res, "colleagues": colleagues_res, "company": company_res}

        return HttpResponse(json.dumps(result_data, ensure_ascii=False))


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['interview']


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SurveyQuestionsSerializer(instance)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
