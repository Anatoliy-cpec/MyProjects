from django.apps import AppConfig

import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals  # выполнение модуля -> регистрация сигналов


r = redis.Redis(
  host='********************************',
  port=10479,
  password='********************************')