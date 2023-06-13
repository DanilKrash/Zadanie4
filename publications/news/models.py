from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    logo = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Логотип')
    image = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Картинка')
    text = models.TextField(blank=False, verbose_name='Текст')
    hidden = models.BooleanField(default=True, verbose_name='Опубликовать')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['date']


class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ForeignKey(Record, on_delete=models.CASCADE, verbose_name='Картинка', related_name='comments')
    text = models.TextField(blank=False, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'