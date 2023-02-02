from django.urls import path, include
from  . import views
from .views import VideoSearchApiView,FamVideoApiView

urlpatterns = [
	path('api/search/', VideoSearchApiView.as_view()),
	path('api/video/', FamVideoApiView.as_view()),
]