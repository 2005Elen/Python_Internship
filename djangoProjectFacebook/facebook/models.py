from django.db import models
GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)
RELATIONSHIP = (
    ('1', 'Single'),
    ('2', 'In a relationship'),
    ('3', 'Engaged'),
    ('4', 'Married'),
    ('5', 'In a civil union'),
    ('6', 'In an open relationship'),
    ('7', 'In a domestic partnership')
)

DEGREE = (
    ('1', 'Associate degrees'),
    ('2', "bachelor's degrees"),
    ('3', "master's degrees"),
    ('4', "doctor's degrees"),
)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    last_login = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='media/photos', blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP, blank=True, null=True)
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    degree = models.CharField(max_length=1, choices=DEGREE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField()
    created_at = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField()
    position = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.position

class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    attemted_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.otp

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class CategoryOfProduct(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField()
    def __str__(self):
        return self.name
class DitailOfProduct(models.Model):
    title = models.CharField(max_length=30)
    discription = models.TextField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=20)
    price = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='media/photos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    def __str__(self):
        return self.title
class Product(models.Model):
    category = models.ForeignKey(CategoryOfProduct, on_delete=models.CASCADE)
    ditail = models.ForeignKey(DitailOfProduct, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/photos', blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    emoji_photo = models.ImageField(upload_to='media/photos', blank=True, null=True)
    emoji_name = models.CharField(max_length=10)
    def __str__(self):
        return self.emoji_name

