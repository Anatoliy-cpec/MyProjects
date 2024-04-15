from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostSearchForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'choise',
           'category',
         #   'creation_date',
       ]

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['choise', 'post_header', 'post_text', 'author', 'category']
    
    def clean(self):
            
            cleaned_data = super().clean()
            post_text = cleaned_data.get("post_text")
            if post_text is not None and len(post_text) < 20:
                raise ValidationError({
                    "post_text": "Текст не может быть менее 20 символов."
                })
            
            post_header = cleaned_data.get("post_header")
            if post_header is not None and len(post_header) > 20:
                 raise ValidationError({
                    "post_header": "Заголовок не может быть более 20 символов."
                 })
            
            if post_text == post_header:
                 raise ValidationError({
                    "post_text": "Текст и заголовок не могут быть одинаковыми.",
                    "post_header": "Текст и заголовок не могут быть одинаковыми."
                 })
            return cleaned_data    

class PostNewsForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = [ 'post_header', 'post_text', 'author', 'category']
    
    def clean(self):
            
            cleaned_data = super().clean()
            post_text = cleaned_data.get("post_text")
            if post_text is not None and len(post_text) < 20:
                raise ValidationError({
                    "post_text": "Текст не может быть менее 20 символов."
                })
            
            post_header = cleaned_data.get("post_header")
            if post_header is not None and len(post_header) > 20:
                 raise ValidationError({
                    "post_header": "Заголовок не может быть более 20 символов."
                 })
            
            if post_text == post_header:
                 raise ValidationError({
                    "post_text": "Текст и заголовок не могут быть одинаковыми.",
                    "post_header": "Текст и заголовок не могут быть одинаковыми."
                 }) 
            
            return cleaned_data 
    
class PostArticleForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = [ 'post_header', 'post_text', 'author', 'category']
    
    def clean(self):
            
            cleaned_data = super().clean()
            post_text = cleaned_data.get("post_text")
            if post_text is not None and len(post_text) < 20:
                raise ValidationError({
                    "post_text": "Текст не может быть менее 20 символов."
                })
            
            post_header = cleaned_data.get("post_header")
            if post_header is not None and len(post_header) > 20:
                 raise ValidationError({
                    "post_header": "Заголовок не может быть более 20 символов."
                 })
            
            if post_text == post_header:
                 raise ValidationError({
                    "post_text": "Текст и заголовок не могут быть одинаковыми.",
                    "post_header": "Текст и заголовок не могут быть одинаковыми."
                 })
            
            return cleaned_data 

