from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100,default="")
    title =models.CharField(max_length=100,default="")
    id = models.AutoField(primary_key=True)
    short_desc =models.CharField(max_length=200,default="")
    content =RichTextField()
    thumbnail =models.ImageField(upload_to="blogimages")
    created_at =models.TimeField(auto_now_add=True)




def __str__(self):
    return self.title()


class comment(models.Model):
    name = models.CharField(max_length=100,default="")
    blogparent = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now=True)



def __str__(self):
    return self.name
    


class Reply(models.Model):
    name = models.CharField(max_length=100,default="") 
    commentparent = models.ForeignKey(comment,on_delete=models.CASCADE)
    Reply = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


def __str__(self):
     return self.name
   