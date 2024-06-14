from django.contrib import admin
from .translations import PostTranslationOptions, CategoryTranslationOptions
from .models import Post, Category
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)

 
class PostAdmin(TranslationAdmin):
    model = Post

class CategoryAdmin(TranslationAdmin):
    model = Category



 
  
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)