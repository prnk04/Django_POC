from django.db import models

# Create your models here.

class KeywordsMapping(models.Model):
    key_id = models.IntegerField()
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.key_id} : {self.keyword}"


class AuthorsTable(models.Model):
    author_id = models.IntegerField(unique=True)
    author_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.author_id} : {self.author_name}"

class ResourceIdentification(models.Model):
    resource_id = models.IntegerField()
    resource_name = models.CharField(max_length = 400)

    def __str__(self):
        return f"{self.resource_id} : {self.resource_name}"

class Contributions(models.Model):
    author_id = models.ForeignKey(AuthorsTable, on_delete= models.CASCADE, related_name= "Contribution")
    resource_id = models.ForeignKey(ResourceIdentification, on_delete= models.CASCADE, related_name= "ContributedResource")

    def __str__(self):
        return f"{self.author_id} : {self.resource_id}"

class ImgResource(models.Model):
    resource_id = models.ForeignKey(ResourceIdentification, on_delete= models.CASCADE, related_name= "ContributedResources")
    key_id = models.ForeignKey(KeywordsMapping, on_delete= models.PROTECT, related_name= "keywords")
    dateSubmitted = models.DateField(auto_now_add=True)
    link = models.URLField()
    resourceFile = models.BinaryField()


# admin creds: prtkprnk35 143@Prat