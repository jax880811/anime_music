from django.db import models

# Create your models here.
class AnimeSong(models.Model):
    song_name = models.CharField(max_length=45, primary_key=True, db_column='歌曲名稱')  # 對應欄位 `歌曲名稱`
    work_name = models.CharField(max_length=45, null=True, db_column='作品名稱')       # 對應欄位 `作品名稱`
    season_or_other = models.CharField(max_length=45, null=True, db_column='季度或其他') # 對應欄位 `季度或其他`
    broadcast_year = models.IntegerField(null=True, db_column='播出年份')             # 對應欄位 `播出年份`
    broadcast_month = models.IntegerField(null=True, db_column='播出月份')            # 對應欄位 `播出月份`
    singer_or_group = models.CharField(max_length=45, null=True, db_column='歌手或者其他團體')             # 對應欄位 `歌手`

    class Meta:
        db_table = 'anime_song'  # 對應資料庫中的表名稱