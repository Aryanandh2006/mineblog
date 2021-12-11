from django.urls import path
#from . import views
from .views import HomeView, ArticleDetail, AddPostView, UpdatePostView, DeletePostView
from django.views.generic import TemplateView


urlpatterns = [
    #path('', views.home, name='home'),
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('blog/', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', ArticleDetail.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
]

