from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Question, Interview, Grade, Survey, Category
from .serializers import QuestionSerializer, InterviewSerializer, \
    GradeSerializer, SurveySerializer, InterviewSurveyQuesitonSerializer, CategorySerializer,\
    SurveyQuestionsSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticated] //TODO
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
    # permission_classes = [IsAuthenticated] //TODO

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterviewSurveyQuesitonSerializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_interviews(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # def get_queryset(self): //TODO
    #     self.queryset = Interview.objects.filter(user=self.request.user)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    # permission_classes = [IsAuthenticated] //TODO
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
