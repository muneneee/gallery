from django.db import models

class Photo(models.Model):
    image= models.ImageField(upload_to='photos/')
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location' on_delete=models.CASCADE) 