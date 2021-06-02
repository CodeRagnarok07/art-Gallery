from django.db import models
from django.db.models.fields import BooleanField, DateField, DateTimeField, FloatField, IntegerField, SlugField

from io import BytesIO
from django.core.files import File
from PIL import Image


from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = SlugField(max_length=50,null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):    #luego agregamos esta funcion a la clase para que se agrege el titulo como slug
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):

    ## segmentcion ##
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255, null=True, blank=True)
    slug = SlugField(default="delalo_vacio" ,max_length=50, unique=True)

    ## venta ##    
    price = FloatField()


    ## ##
    buy_link = models.TextField()
    date_add = DateTimeField(auto_now_add=True)
    ### imagen ###
    image = models.ImageField(blank=True ,null=True)
    tumbnail = models.ImageField(blank=True ,null=True)

    def __str__(self):
        return self.title

        
    #ejecucion automatica
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        #self.image.name = self.title + ".jpg" # va a ayudar con el seo
        self.tumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    #crear la tumbnail automatica

    def make_thumbnail(self, image, size=(600, 400)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name= "thumbnail_"+ image.name)

        return thumbnail



