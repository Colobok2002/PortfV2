# Generated by Django 4.1.2 on 2022-10-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='photo',
            field=models.ImageField(blank=True, upload_to='img/site', verbose_name='Обложка'),
        ),
    ]
