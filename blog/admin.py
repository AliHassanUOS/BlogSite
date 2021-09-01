from django.contrib import admin
from .models import Blog_model
# Register your models here.


class Blog_Model_Admin(admin.ModelAdmin):

    list_display = ["id",'author',"title"]
    list_display_links= ["author","title"]
    search_fields = ["id","author"]
    list_filter = ["id",'author',"title"]


admin.site.register(Blog_model,Blog_Model_Admin)
