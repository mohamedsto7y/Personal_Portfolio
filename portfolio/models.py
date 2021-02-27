from django.db import models

# Create your models here.
class Project(models.Model):
    titleman=models.CharField (max_length=50)
    description=models.CharField( max_length=50)
    image=models.ImageField( upload_to='portfolio/images/', height_field=None, width_field=None, max_length=None)
    url=models.URLField(blank=True)
    def __str__(self):
       return self.titleman



   
   
