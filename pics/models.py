from django.db import models



class Location(models.Model):
    location_name=models.CharField(max_length=20)


    @classmethod
    def get_location_id(cls, id):
        place = Location.objects.get(pk = id)
        return place


    def __str__(self):
        return self.location_name

   


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Photo(models.Model):
    image= models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE) 
    posted = models.DateTimeField(auto_now_add=True)


    

    def save_photo(self):
        self.save()


    @classmethod
    def filter_by_location(cls,location):
        pics_location = cls.objects.filter(location__id=location)
        return pics_location


    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(category__category_name__icontains=search_term)
        return pics


    def __str__(self):
        return self.name

