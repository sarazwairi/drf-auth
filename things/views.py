from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from django.shortcuts import render
from .serializers import PostSerializer
from .models import Things
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class ThingsList(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    queryset=Things.objects.all()
    serializer_class=PostSerializer

class ThingsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Things.objects.all()
    serializer_class=PostSerializer

