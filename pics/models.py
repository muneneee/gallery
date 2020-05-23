from django.db import models

class Photo(models.Model):
    image= models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location' on_delete=models.CASCADE) 


    def __str__(self):
        return self.name


class Location(models.Model):
    location_name=models.CharField(max_length=20)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name