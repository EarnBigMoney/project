from django.db import models

#书籍表
class Book(models.Model):\

    book_src = models.CharField(max_length=150,verbose_name='图片地址',
                                blank=True)

    book_title = models.CharField(max_length=20,verbose_name='书籍名称',
                                  blank=True)

    book_author = models.CharField(max_length=20,verbose_name='作者',
                                   blank=True)

    book_style = models.CharField(max_length=20,verbose_name='类型',
                                  blank=True)

    book_publish = models.CharField(max_length=20,verbose_name='出版社',
                                    blank=True)

    book_words = models.CharField(max_length=20,verbose_name='字数',
                                  blank=True)

    book_price = models.FloatField(max_length=20,verbose_name='全本定价',
                                   blank=True)

    book_pre = models.TextField(max_length=1000,verbose_name='导言',
                                blank=True)

    book_hits = models.IntegerField(verbose_name='点击量')

    is_delete = models.IntegerField(default='0', choices=((0, '否'), (1, '是')), verbose_name='是否删除')

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







