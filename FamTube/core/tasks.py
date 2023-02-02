from FamTube.celery import app
from .celery_handlers.beats import youtube_video_consumer
from celery import shared_task

@shared_task
def pull_videos():
    print("pulling videos ------------------")
    youtube_video_consumer()
