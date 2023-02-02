from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .handlers import video_search_handler, get_all_videos


class VideoSearchApiView(APIView):

	def get(self, request):
		videos = video_search_handler(request)
		return videos
	

class FamVideoApiView(APIView):
	
	def get(self, request):
		videos = get_all_videos(request)
		return videos
