from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project_info(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    author = models.CharField(max_length=100)
    numOfTemplate = models.IntegerField()
    createdate = models.DateTimeField()
    updatedate = models.DateTimeField()
        
    def __str__(self):
        return self.title

#runing env in all projects
#class Environment(models.Model):pass
    #name = models.CharField(max_length = 100,unique = True)

#class Template(models.Model):
#   pass
    #title = models.CharField(max_length = 140)
    #description = models.TextField()
    #createdate = models.DateTimeField()
    #updatedate = models.DateTimeField(default = createdate)

#class Resource(models.Model):
#   pass
    #name = models.CharField(max_length = 140,unique = True)

#class User(models.Model):
#    pass
    #username = models.CharField(max_length = 100)
    #photo = models.ImageField(upload_to = "upload_img", default = "upload_img/default.jpg")
    #email = models.CharField(max_length = 30)

