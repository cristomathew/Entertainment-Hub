from django.db import models
from sub_categories.models import SubCategory
# Create your models here.

class Entertainment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    season = models.IntegerField(default="1")
    video = models.FileField(upload_to='videos/Entertainment/')

    def __str__(self):
        return self.title