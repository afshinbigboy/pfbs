from django.urls import path
from .views import *


app_name = 'feedbacks'


urlpatterns = [
    path('presentation', presentation, name='presentation'),
]
