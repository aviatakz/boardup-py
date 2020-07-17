from django.urls import path, include
from rest_framework.routers import DefaultRouter
from survey import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename='SurveyQuestions')
router.register(r'interviews', views.InterviewViewSet, basename="UserInterviews")
router.register(r'grades', views.GradeViewSet, basename='Grades')
router.register(r'survey', views.SurveyViewSet, basename="Survey")

urlpatterns = [
    path('', include(router.urls))
]