from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

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
                    "post_text": _("The text cannot be less than 20 characters long.")
                })
            
            post_header = cleaned_data.get("post_header")
            if post_header is not None and len(post_header) > 20:
                 raise ValidationError({
                    "post_header": _("The header cannot be more than 20 characters long.")
                 })
            
            if post_text == post_header:
                 raise ValidationError({
                    "post_text": _("The text and the title cannot be the same."),
                    "post_header": _("The text and the title cannot be the same."),
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
                    "post_text": _("The text cannot be less than 20 characters long.")
                })
            
            post_header = cleaned_data.get("post_header")
            if post_header is not None and len(post_header) > 20:
                 raise ValidationError({
                    "post_header": _("The header cannot be more than 20 characters long.")
                 })
            
            if post_text == post_header:
                 raise ValidationError({
                    "post_text": _("The text and the title cannot be the same."),
                    "post_header": _("The text and the title cannot be the same."),
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
                    "post_text": _("The text cannot be less than 20 characters long.")
                })
            
            post_header = cleaned_data.get("post_header")
            if post_header is not None and len(post_header) > 20:
                 raise ValidationError({
                    "post_header": _("The header cannot be more than 20 characters long.")
                 })
            
            if post_text == post_header:
                 raise ValidationError({
                    "post_text": _("The text and the title cannot be the same."),
                    "post_header": _("The text and the title cannot be the same."),
                 })
            
            return cleaned_data 

