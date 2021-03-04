from django.http import HttpRequest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
import requests
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.
class FeedLCView(ListCreateAPIView):
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()


class FeedRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()


class GetFeed(RetrieveAPIView):
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()

    def retrieve(self, request, *args, **kwargs):
        feed = Feed.objects.get(id=kwargs.get('pk'))
        http_request = requests.get(feed.url)
        print(http_request.text)
        return Response(http_request.text, status=200)
