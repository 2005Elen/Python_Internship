from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='client/')
    review = models.TextField(max_length=500)

    def __str__(self):
        return self.name
