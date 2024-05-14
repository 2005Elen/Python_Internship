from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Service(TimeStampedModel):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, max_length=30)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='service/')

    def __str__(self):
        return self.title

