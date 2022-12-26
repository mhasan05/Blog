from django.db import models

# Create your models here.
class NewPost(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='postimages/', default='postimages/default.png',null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    