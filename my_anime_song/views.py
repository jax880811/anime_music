
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
# Create your views here.
from my_anime_song.models import AnimeSong
from my_anime_song.serializers import MusicSerializer

class MusicViewSet(viewsets.ModelViewSet):
    queryset = AnimeSong.objects.all()
    serializer_class = MusicSerializer
