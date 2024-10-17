from django.urls import path
from Home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('art_list/', views.art_list, name='art_list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('create_article/', views.create_article, name='create_article'),
    path('edit_article/<int:article_id>', views.edit_article, name='edit_article'),
    path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),
    path('article_category/<int:category_id>', views.get_article_by_category, name='article_category'),
    path('article_author/<int:author_id>', views.get_article_by_author, name='article_author'),
]