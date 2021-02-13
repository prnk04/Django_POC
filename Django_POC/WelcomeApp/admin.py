from django.contrib import admin
from .models import  ImgResource, VideoResource, ArticleResource

# Register your models here.

admin.site.register(ImgResource)
admin.site.register(VideoResource)
admin.site.register(ArticleResource)
