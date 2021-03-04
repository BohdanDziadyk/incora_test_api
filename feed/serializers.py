from rest_framework.serializers import ModelSerializer
from .models import *


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
