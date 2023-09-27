from django.contrib import admin

# Register your models here.
from .models import BlogPost
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display=["Title","author","publish_on","Description"]
 