import datetime


from django.forms import DateTimeInput
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category



class PostSearchFilter(FilterSet):
   
   
   post_header = CharFilter(lookup_expr='icontains')
   category = ModelChoiceFilter(queryset=Category.objects.all())
   creation_date = DateTimeFilter(
            lookup_expr='gt', 
            widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ))
   
   
   class Meta:
       
       model = Post
       fields = {
           
       }
            
