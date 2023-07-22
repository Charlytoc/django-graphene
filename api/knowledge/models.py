from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    username=models.CharField(max_length=255, unique=True)
    age=models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    
