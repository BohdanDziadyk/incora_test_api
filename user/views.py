from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.

class LogInView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        try:
            user = User.objects.get(username=self.request.data.__getitem__('username'))
        except Exception:
            return Response('Given credentials is not valid for any active user', status=401)
        else:
            if user.password == self.request.data.__getitem__('password'):
                return Response('User succsessfully authorized', status=200)
            else:
                return Response('Given credentials is not valid for any active user', status=401)
