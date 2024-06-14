# Generated by Django 5.0.3 on 2024-06-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_en_us',
            field=models.CharField(max_length=24, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_ru',
            field=models.CharField(max_length=24, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_header_en_us',
            field=models.CharField(help_text='Место для заголовка', max_length=64, null=True, verbose_name='Post header'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_header_ru',
            field=models.CharField(help_text='Место для заголовка', max_length=64, null=True, verbose_name='Post header'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text_en_us',
            field=models.TextField(default='Some text', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text_ru',
            field=models.TextField(default='Some text', max_length=512, null=True),
        ),
    ]
