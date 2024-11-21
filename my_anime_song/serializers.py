from rest_framework import serializers
from my_anime_song.models import AnimeSong


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeSong
        fields = '__all__'
        