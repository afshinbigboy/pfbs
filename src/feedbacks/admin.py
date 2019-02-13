from django.contrib import admin
from .models import Question, Presentation, Feedback

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('rank', 'title', 'description')
    search_fields = ('description', 'title')


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'oral_date')
    list_filter = ('oral_date',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'presentation', 'score', 'question')
    list_filter = ('student', 'presentation', 'score')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Feedback, FeedbackAdmin)
