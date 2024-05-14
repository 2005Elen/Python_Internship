from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    review = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name
