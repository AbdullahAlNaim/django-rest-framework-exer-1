from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import IndieGame
from .serializers import IndieGameSerializer


# Create your views here.
class GameDevView(generics.ListCreateAPIView):
    queryset = IndieGame.objects.all()
    serializer_class = IndieGameSerializer
    
class SingleGameView(generics.RetrieveDestroyAPIView):
    queryset = IndieGame.objects.all()
    serializer_class = IndieGameSerializer

