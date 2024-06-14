from django.urls import path
<<<<<<< Updated upstream

from .views import * 

=======
from .views import (
    PostsList,
    PostSearch,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete,
    PostArticleCreate,
    PostArticleUpdate,
    PostArticleDelete,
    PostNewsCreate,
    PostNewsUpdate,
    PostNewsDelete,

)
>>>>>>> Stashed changes


urlpatterns = [
   path('', PostsList.as_view(), name='posts'), 
   path('search/', PostSearch.as_view(), name='search'), 
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('articles/create/', PostArticleCreate.as_view(), name='article_create'),
   path('news/create/', PostNewsCreate.as_view(), name='news_create'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('edit/<int:pk>/', PostUpdate.as_view(), name='post_edit'),
   path('articles/edit/<int:pk>/', PostArticleUpdate.as_view(), name='article_edit'),
   path('news/edit/<int:pk>/', PostNewsUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('news/delete/<int:pk>/', PostNewsDelete.as_view(), name='news_delete'),
<<<<<<< Updated upstream
   path('articles/delete/<int:pk>/', PostArticleDelete.as_view(), name='article_delete'),
   
]
=======
   path('articles/delete/<int:pk>/',
        PostArticleDelete.as_view(), name='article_delete'),
]
>>>>>>> Stashed changes
