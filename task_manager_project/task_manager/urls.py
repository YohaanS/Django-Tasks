from django.urls import path
from . import views

urlpatterns = [
    # URL for the main page (tasks)
    path('', views.index, name='tasks'),
]
