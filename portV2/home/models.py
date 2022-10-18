from django.db import models

# Create your models here.

class Projekt(models.Model):


    name = models.CharField(max_length=200, db_index=True,verbose_name='Название проэкта')
    slug = models.SlugField(max_length=200, db_index=True,verbose_name='Уникальный url')
    opis = models.CharField(max_length=200, db_index=True, verbose_name='Описание')
    photo = models.ImageField(upload_to=f'img/site', blank=True,verbose_name='Обложка')
    available = models.BooleanField(default=True,verbose_name='Актуальность')
    utl_git = models.CharField(max_length=200, db_index=True,verbose_name='Url гитхаба')
