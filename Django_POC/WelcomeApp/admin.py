from django.contrib import admin
from .models import KeywordsMapping, ImgResource, AuthorsTable, ResourceIdentification, Contributions

# Register your models here.
admin.site.register(KeywordsMapping)
admin.site.register(ImgResource)
admin.site.register(AuthorsTable)
admin.site.register(ResourceIdentification)
admin.site.register(Contributions)