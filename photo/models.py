from django.db import models

class Photo(models.Model):
   
    slug = models.SlugField(max_length=50, default="none" )
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.title