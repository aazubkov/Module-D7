from django.urls import path
from .views import NewsList, NewsId, PostSearch, PostEdit, PostDelete, NewsCreate, ArticlesCreate

urlpatterns = [
   path('', NewsList.as_view(), name='post_list'),

   path('news/', NewsList.as_view(), name='post_list'),
   path('news/<int:pk>', NewsId.as_view(), name='post_id_view'),
   path('news/<int:pk>/edit', PostEdit.as_view()),
   path('news/<int:pk>/delete', PostDelete.as_view()),
   path('news/search/', PostSearch.as_view()),
   path('articles/', NewsList.as_view()),
   path('articles/<int:pk>', NewsId.as_view()),
   path('articles/<int:pk>/edit', PostEdit.as_view()),
   path('articles/search/', PostSearch.as_view()),
   path('articles/<int:pk>/delete', PostDelete.as_view()),

   path('articles/create/', ArticlesCreate.as_view()),
   path('news/create/', NewsCreate.as_view()),
]
