from django.contrib import admin
from facebook.models import (User, Education, Job, Otp,
                             Game, CategoryOfProduct, DitailOfProduct,
                             Product, Post, Comment, Like)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name',)
    ordering = ('-created_at',)

admin.site.register(User, UserAdmin)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(Otp)
admin.site.register(Game)
admin.site.register(CategoryOfProduct)
admin.site.register(DitailOfProduct)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

