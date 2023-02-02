from datetime import datetime, timedelta
from core.models import FamVideo
from core.constants import API_KEYS
from googleapiclient.discovery import build
import json
from random import randint, choice
ACTIVE_API_KEY_INDX = 0


def prepare_youtube_api():
    search_query = ["World Affairs", "FamPay", "India", "Arijit Singh", "Coke Studio"]
    request = build('youtube', 'v3', developerKey=API_KEYS[ACTIVE_API_KEY_INDX])
    query = choice(search_query)
    response = request.search().list(
                q=query,
                part="snippet",
                maxResults=30,
                type='video',
                order='date',
                publishedAfter=str((datetime.today() - timedelta(days=randint(1,2000))).strftime("%Y-%m-%dT%H:%M:%SZ")),
    )
    return response

def get_valid_api_key():
    global ACTIVE_API_KEY_INDX
    ACTIVE_API_KEY_INDX = (ACTIVE_API_KEY_INDX + 1) % len(API_KEYS) # make it circular
    api_key = API_KEYS[ACTIVE_API_KEY_INDX]
    return api_key

def youtube_video_consumer():
    try:
        request = prepare_youtube_api()
        response = request.execute().get('items', [])
        video_objects = [
            FamVideo(
                title=video['snippet']['title'],
                description=video['snippet']['description'],
                published_on=datetime.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
                small_thumbnail=video['snippet']['thumbnails']['default']['url'],
                medium_thumbnail=video['snippet']['thumbnails']['medium']['url'],
                large_thumbnail=video['snippet']['thumbnails']['high']['url']
            )
            for video in response
        ]
        FamVideo.objects.bulk_create(video_objects)

    except Exception as ex: 
        print("Exception in youtube_video_consumer: ", str(ex))
        get_valid_api_key()
