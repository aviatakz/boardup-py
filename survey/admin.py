from django.contrib import admin
from survey.models import Grade, Question, Interview, Category, Survey


class GradeAdmin(admin.ModelAdmin):
    model = Grade
    list_display = ('value', 'get_description', 'interview', 'created_at')

    def get_description(self, obj):
        return obj.question.description

    get_description.short_description = "Question"

    def get_interview_target(self, obj):
        return obj.interview.target_user.username

    get_interview_target.short_description = "Targeted person"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'survey')


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_user', 'comment', 'created_at')


admin.site.register(Grade, GradeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Survey)
