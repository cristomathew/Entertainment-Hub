from django.db import models
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
# Create your models here.
categorychoices = {
  ('Comedy', 'Comedy'),
  ('Action', 'Action'),
  ('Drama', 'Drama'),
  }
class Category(models.Model):
    title = models.CharField(max_length=200)
    image = fields.ImageField(upload_to='category',blank=True, dependencies=[
        FileDependency(attname='avatar_jpeg', processor=ImageProcessor(
            format='JPEG', scale={'max_width': 500, 'max_height': 600})),
    ])
    description = models.TextField(blank=True)
    typ= models.CharField(max_length=100,choices=categorychoices,default="Comedy")
    def __str__(self):
        return self.title