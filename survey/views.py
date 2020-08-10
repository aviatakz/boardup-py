import json

from django.db.models import Avg
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'target_user', 'survey']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterviewSurveyQuesitonSerializer(instance)
        return Response(serializer.data)

    @action(detail=False)
    def results(self, request):
        user_id = request.GET["user_id"]
        survey_id = request.GET["survey_id"]

        grades = Grade.objects.values('question__category').annotate(avg=Avg('value'))
        company = grades.filter(interview__survey=survey_id)
        colleagues = grades.filter(interview__survey=survey_id, interview__target_user=user_id).exclude(
            interview__user=user_id
        )
        selff = grades.filter(interview__survey=survey_id, interview__target_user=user_id,
                              interview__user=user_id)
        categories = CategorySerializer(Category.objects.all(), many=True)

        res = {"categories": categories.data, "self": list(selff), "colleagues": list(colleagues),
               "company": list(company)}
        return HttpResponse(json.dumps(res, ensure_ascii=False))
      
    @action(detail=False, methods=['post'])
    def create_interviews(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['interview']


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveyQuestionsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
