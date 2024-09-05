from django.urls import path
from . import views



app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/posts/', views.post, name='list_of_posts'),
    path('tag/<slug:tag_slug>/', views.post, name='posts_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:post_slug>/comment/', views.post_comment, name='post_comment'),
    path('about-me/', views.about, name='about'),
    path('search/', views.search, name='search')
    ]