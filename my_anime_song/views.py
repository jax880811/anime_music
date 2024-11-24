
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action

from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
# Create your views here.
from my_anime_song.models import AnimeSong
from my_anime_song.serializers import MusicSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.views import View

class SearchMusicView(View):
    template_name = 'search_music.html'  # 模板檔案名稱

    def get(self, request):
        # 獲取查詢字串（音樂名稱）
        query = request.GET.get('q', '')  # 默認為空字串
        results = []

        all_songs = AnimeSong.objects.all()  # 使用 Django ORM 查詢所有歌曲

        if query:
            # 使用原生 SQL 查詢 MySQL 資料庫
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 歌曲名稱, 音樂網址
                    FROM anime_song
                    WHERE 歌曲名稱 LIKE %s
                """, [f"%{query}%"])
                results = cursor.fetchall()

        # 傳遞資料到模板，供前端渲染
        return render(request, self.template_name, {
            'query': query, 
            'results': results,
            'all_songs': all_songs  # 傳遞所有歌曲
        })

'''
class SearchMusicView(ViewSet):
    @action(detail=False, methods=['get'], url_path='search')
    def search_music(self, request):
        query = request.GET.get('q', '')
        results = []

        if query:
            results = AnimeSong.objects.filter(歌曲名稱__icontains=query).values('歌曲名稱', '音樂網址')

        return Response({'query': query, 'results': list(results)})
'''   

class MusicViewSet(viewsets.ModelViewSet):
    queryset = AnimeSong.objects.all()
    serializer_class = MusicSerializer
