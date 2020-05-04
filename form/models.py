from django.db import models

# Create your models here.
class entry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    fb = models.CharField(max_length=200,blank=True, null=True)
    insta = models.CharField(max_length=100,blank=True, null=True)
    quote = models.CharField(max_length=500)
    photograph = models.ImageField(upload_to='')

    def __str__(self):
        return self.name
