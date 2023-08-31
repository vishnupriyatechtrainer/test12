from django.db import models

# Create your models here.


class aboutnew(models.Model):
    title =models.CharField(max_length=100,blank=False)
    description =models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)

    # def __str__(self):
    #     return self.title


class visitor(models.Model):
    title =models.CharField(max_length=100,blank=False)
    description =models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='visitor/',blank=False)


class client(models.Model):
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='client/',blank=False)
