from django.contrib import admin
from .models import (User, Category, SubCategory, Ads, AdsDetails, Otp,
                     Payment, Wallet, Massages)
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Ads)
admin.site.register(AdsDetails)
admin.site.register(Otp)
admin.site.register(Payment)
admin.site.register(Wallet)
admin.site.register(Massages)
