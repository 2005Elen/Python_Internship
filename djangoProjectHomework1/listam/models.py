from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField()
    last_login = models.DateTimeField(null=True)
    ip_address = models.GenericIPAddressField(max_length=16, unique=True, null=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    photo = models.ImageField(upload_to='media/photo/', null=True, blank=True)
    def __str__(self):
        return self.first_name
class Category(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField()
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.name

class AdsDetails(models.Model):
    location = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='media/photo/', null=True, blank=True)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Ads(models.Model):
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    views = models.SmallIntegerField()

class Massages(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ads_id = models.ForeignKey(Ads, on_delete=models.CASCADE)
    text = models.TextField()


class Otp(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    attended_at = models.DateTimeField()

class Payment(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Wallet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateTimeField()
    status = models.BooleanField()



