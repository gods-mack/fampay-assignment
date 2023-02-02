from .models import FamVideo
from .utils import  CustomPaginator
from django.db.models import Q


def partial_query_handler(partial_query):
    # videos will now contain all FamVideo objects that match all the words in the partial_query.
    words = partial_query.split()
    for indx, word in enumerate(words):
        if indx == 0:
            videos = FamVideo.objects.filter(Q(title__icontains=word) | Q(description__icontains=word))
        else:
            videos = videos.filter(Q(title__icontains=word) | Q(description__icontains=word))
    return videos


def video_search_handler(request):
    param_q = request.GET
    title, desc = param_q.get('title'), param_q.get('description')
    partial_query = param_q.get('partial_query')

    if title and desc:
        videos = FamVideo.objects.filter(Q(title__icontains=title) | Q(description__icontains=desc))
    elif title:
        videos = FamVideo.objects.by_title(title)
    elif desc:
        videos = FamVideo.objects.by_description(desc)
    elif partial_query:
        videos = partial_query_handler(partial_query)  # "How to make tea" -> "tea how"
    else:
        videos = FamVideo.objects.get_all()
    
    return CustomPaginator().paginated_resp(videos, FamVideo.serializer, request)


def get_all_videos(request):
    videos = FamVideo.objects.get_all()
    return CustomPaginator().paginated_resp(videos, FamVideo.serializer, request)
