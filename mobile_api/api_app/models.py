from django.db import models
from django.conf import settings

class Posts(models.Model):

     title = models.CharField(max_length=255)
     content = models.TextField(blank=True)
     username= models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь",on_delete=models.CASCADE,default=1)

     def __str__(self):
          return self.title


