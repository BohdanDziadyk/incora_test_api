from django.urls import path
from .views import *

urlpatterns = [
    path('', FeedLCView.as_view()),
    path('<int:pk>', FeedRUDView.as_view()),
    path('get_feed/<int:pk>', GetFeed.as_view())
]
