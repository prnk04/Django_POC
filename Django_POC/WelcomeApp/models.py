from django.db import models
# from PIL import *

# Create your models here.

class ImgResource(models.Model):
    resource_name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    keywords = models.CharField(max_length=500)
    dateSubmitted = models.DateField(auto_now_add=True)
    link = models.URLField(blank=True)
    resourceFile = models.ImageField(blank=True, upload_to='imageResources')

    def __str__(self):
        if self.link == '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.resourceFile}"
        if self.resourceFile == '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.link}"
        if self.link != '' and self.resourceFile != '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.link} and {self.resourceFile}"
     
    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['resource_name', 'authors'], name='unique_article'),
        models.CheckConstraint(
                name="resourcePresent",
                check=(
                    ~models.Q( 
                        resourceFile__exact = '',
                        link__exact = ''
                    )
                ),
            )

        ]

class VideoResource(models.Model):
    resource_name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    keywords = models.CharField(max_length=500)
    dateSubmitted = models.DateField(auto_now_add=True)
    link = models.URLField(blank=True)
    resourceFile = models.FileField(blank=True, upload_to='videoResources')

    def __str__(self):
        if self.link == '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.resourceFile}"
        if self.resourceFile == '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.link}"
        if self.link != '' and self.resourceFile != '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.link} and {self.resourceFile}"
        

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['resource_name', 'authors'], name='unique_videoResources'),
        models.CheckConstraint(
                name="videoPresent",
                check=(
                    ~models.Q( 
                        resourceFile__exact = '',
                        link__exact = ''
                    )
                ),
            )

        ]
        


class ArticleResource(models.Model):
    resource_name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    keywords = models.CharField(max_length=500)
    dateSubmitted = models.DateField(auto_now_add=True)
    link = models.URLField(blank=True)
    resourceFile = models.FileField(blank=True, upload_to='articleResources')

    def __str__(self):
        if self.link == '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.resourceFile}"
        if self.resourceFile == '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.link}"
        if self.link != '' and self.resourceFile != '':
            return f"{self.resource_name} is contributed by {self.authors} on {self.dateSubmitted} See here {self.link} and {self.resourceFile}"
        

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['resource_name', 'authors'], name='unique_articleResources'),
        models.CheckConstraint(
                name="articlePresent",
                check=(
                    ~models.Q( 
                        resourceFile__exact = '',
                        link__exact = ''
                    )
                ),
            )

        ]
        
    


# admin creds: prtkprnk35 143@Prat