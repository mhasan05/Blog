from django.urls import path
from blogpost import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('post_',views.AllPost,name="allpost" ),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)