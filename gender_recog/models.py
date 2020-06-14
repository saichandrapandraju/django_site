from django.db import models

# Create your models here.
class Check(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

class CheckF(models.Model):
    for_name = models.ForeignKey(Check,on_delete=models.CASCADE)
    url = models.URLField(max_length=30)

    def __str__(self):
        return self.url

class Image_data(models.Model):
    image = models.FileField(upload_to='uploaded_images/')
