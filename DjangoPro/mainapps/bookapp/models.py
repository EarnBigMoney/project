from django.db import models

#书籍表
class Book(models.Model):
    book_src = models.CharField(max_length=150,verbose_name='图片地址',
                                blank=True, default='')

    book_title = models.CharField(max_length=20,verbose_name='书籍名称',
                                  blank=True, default='')

    book_author = models.CharField(max_length=20,verbose_name='作者',
                                   blank=True, default='')

    book_style = models.CharField(max_length=20,verbose_name='类型',
                                  blank=True, default='')

    book_publish = models.CharField(max_length=20,verbose_name='出版社',
                                    blank=True, default='')

    book_words = models.CharField(max_length=20,verbose_name='字数',
                                  blank=True, default='')

    book_price = models.FloatField(max_length=20,verbose_name='全本定价',
                                   blank=True, default='')

    book_pre = models.TextField(max_length=1000,verbose_name='导言',
                                blank=True, default='')




    book_hits = models.IntegerField(verbose_name='点击量')

    def __str__(self):
        return self.book_title

    class Meta:
        db_table = 't_books'
        verbose_name = '书籍列表'
        verbose_name_plural = verbose_name
        ordering = ['-book_hits']

# class Book_Tag(models.Model):
#
#     t_name = models.CharField(max_length=20,verbose_name='标签名称',
#                               blank=True, default='')
#     t_classify = models.CharField(max_length=20,verbose_name='标签分类',
#                                   blank=True, default='')
#     book_tag = models.ForeignKey(Book,on_delete=models.CASCADE)


'''
# # 电影表
#
# class Movie(models.Model):
#     movie_url = models.CharField(max_length=150,verbose_name='电影图片',
#                                  blank=True, default='')
#
#     movie_name = models.CharField(max_length=20,verbose_name='电影名称',
#                                   blank=True, default='')
#
#     movie_director = models.CharField(max_length=20,verbose_name='导演',
#                                       blank=True, default='')
#
#     movie_adaptor = models.CharField(max_length=20,verbose_name='编剧',
#                                      blank = True,default='')
#
#     movie_actor = models.CharField(max_length=50,verbose_name='主演',
#                                          blank=True, default='')
#
#     movie_style = models.CharField(max_length=20,verbose_name='类型',
#                                    blank=True, default='')
#
#     movie_publish = models.CharField(max_length=30,verbose_name='上映时间',
#                                      blank=True, default='')
#
#     movie_length = models.CharField(max_length=20,verbose_name='片长',
#                                     blank=True, default='')
#
#     movie_detail = models.TextField(max_length=1000,verbose_name='剧情简介',
#                                       blank=True, default='')
#
#     movie_hits = models.IntegerField(max_length=10, verbose_name='点击量')
#
#     def __str__(self):
#         return self.movie_name
#
#     class Meta:
#         db_table = 't_movies'
#         verbose_name = '电影列表'
#         verbose_name_plural = verbose_name
#         ordering = ['-movie_hits']
'''




