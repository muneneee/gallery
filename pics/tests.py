from django.test import TestCase
from .models import Photo,Location,Category


class PhotoTestClass(TestCase):

    def setUp(self):
        self.cat = Category(category_name="fashion")
        self.cat.save()

        self.loc = Location(location_name="Africa")
        self.loc.save()

        self.image = Photo(name='image test', description='my test',location=self.loc,category=self.cat)
        self.image.save()   

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Photo))


    def test_save_photo(self):
        self.image.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos)>0)


    def test_delete_photo(self):
        self.image.delete_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) < 1)

    

    def test_search_by_category(self):
        images = Photo.search_by_category('fashion')
        self.assertTrue(len(images)>0)



    def test_filter_by_location(self):
        images = Photo.filter_by_location('1')
        self.assertTrue(len(images)>0)
