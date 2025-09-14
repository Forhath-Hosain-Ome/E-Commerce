from django.db import models

# Create your models here.
class Catagory(models.Model):
    catagory_name = models.CharField(unique=True, max_length=50)
    slug = models.CharField(unique=True, max_length=20)
    description = models.TextField()
    catagory_image = models.ImageField(upload_to='photos/catagories', blank=True)

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagory'
        ordering = ['catagory_name']

    def __str__(self):
        return self.catagory_name