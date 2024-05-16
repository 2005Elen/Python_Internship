from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.title