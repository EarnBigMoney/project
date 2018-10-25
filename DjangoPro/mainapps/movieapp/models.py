from django.db import models

# Create your models here.
# 电影表

class Movie(models.Model):

    movie_url = models.CharField(max_length=150,verbose_name='电影图片',
                                 blank=True)

    movie_name = models.CharField(max_length=20,verbose_name='电影名称',
                                  blank=True)

    movie_director = models.CharField(max_length=20,verbose_name='导演',
                                      blank=True)

    movie_adaptor = models.CharField(max_length=20,verbose_name='编剧',
                                     blank = True)

    movie_actor = models.CharField(max_length=50,verbose_name='主演',
                                         blank=True)

    movie_style = models.CharField(max_length=20,verbose_name='类型',
                                   blank=True)

    movie_publish = models.CharField(max_length=30,verbose_name='上映时间',
                                     blank=True)

    movie_length = models.CharField(max_length=20,verbose_name='片长',
                                    blank=True)

    movie_detail = models.TextField(max_length=1000,verbose_name='剧情简介',
                                      blank=True)

    movie_hits = models.IntegerField(verbose_name='点击量')

    is_delete = models.IntegerField(default='0', choices=((0, '否'), (1, '是')), verbose_name='是否删除')

    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 't_movies'
        verbose_name = '电影列表'
        verbose_name_plural = verbose_name
        ordering = ['-movie_hits']

