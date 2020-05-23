from django.test import TestCase
from .models import Photo,Location,Category


class PhotoTestClass(TestCase):

    def setUp(self):
        self.monalisa = Photo(image = 'yg.png', name='monalisa', description  = 'priceless art this is',posted = '2020-03-02')
        self.monalisa.save_photo()

        self.new_category = Category(name = 'test')
        self.new_category.save()

        self.new_location = Location(name = 'test')
        self.new_location.save()

        self.monalisa.Category.add(self.new_category)
        self.monalisa.Location.add(self.new_location)    

    def test_instance(self):
        self.assertTrue(isinstance(self.monalisa,Photo))


    def test_save_photo(self):
        self.monalisa.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos)>0)