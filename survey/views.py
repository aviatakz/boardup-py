from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from survey.models import Question, Interview, Grade, Survey, Category
from survey.serializers import QuestionSerializer, InterviewSerializer, \
    GradeSerializer, SurveySerializer, InterviewSurveyQuesitonSerializer, CategorySerializer


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
        result_data = {}

        self_rating_objects = Grade.objects.filter(interview__survey=survey_id, interview__target_user=user_id,
                                                   interview__user=user_id)
        self_res = average_list(self_rating_objects)
        colleagues_rating_objects = Grade.objects.filter(interview__survey=survey_id, interview__target_user=user_id).exclude(
            interview__user=user_id
        )
        colleagues_res = average_list(colleagues_rating_objects)
        company_rating_objects = Grade.objects.all()
        company_res = average_list(company_rating_objects)

        result_data["self"] = self_res
        result_data["colleagues"] = colleagues_res
        result_data["company"] = company_res

        return HttpResponse(json.dumps(result_data))


def average_list(objects):
    map_self = {}
    list_self = {}
    for grade in objects:
        category = grade.question.category.pk
        if category in map_self:
            map_self[category] += 1
            list_self[category] += grade.value
        else:
            map_self[category] = 1
            list_self[category] = grade.value

    result = {}
    for key, value in map_self.items():
        result[key] = list_self[key] / value

    return result


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['interview']


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
