from django.db import models
# from PIL import *

# Create your models here.

class ImgResource(models.Model):
    resource_name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    keywords = models.CharField(max_length=500)
    dateSubmitted = models.DateField(auto_now_add=True)
    link = models.URLField(blank=True)
    resourceFile = models.ImageField(blank=True)

    def __str__(self):
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
        #  UniqueConstraint(fields=['resource_name', 'authors'], name='unique_article')

    


# admin creds: prtkprnk35 143@Prat