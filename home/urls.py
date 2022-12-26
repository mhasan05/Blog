from django.urls import path
from home import views
urlpatterns = [
    path('',views.Home,name="home" ),
    path('post/<int:id>',views.Post,name="post" ),
    path('author',views.Author,name="author" ),
] 