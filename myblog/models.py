from datetime import datetime
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.

class Blog(models.Model):
    
    blog_name = models.CharField(max_length=100000)
    blog_date = models.DateTimeField(default=datetime.now,blank=True)
    blog_content = models.CharField(max_length=1_000_000_000_000)
    first_image = models.ImageField(upload_to ='images',blank=True, null=True)
    second_image = models.ImageField(upload_to ='images',blank=True, null=True)
    third_image = models.ImageField(upload_to ='images',blank=True, null=True)
    fourth_image = models.ImageField(upload_to ='images',blank=True, null=True)
    fifth_image = models.ImageField(upload_to ='images',blank=True, null=True)
    sixth_image = models.ImageField(upload_to ='images',blank=True, null=True)
    seventh_image = models.ImageField(upload_to ='images',blank=True, null=True)
    
     

    def get_absolute_url(self):
        return self.get_url()

    

    @property
    def simageURL(self):
        try:
            url = self.second_image.url
        except:
            url = ''
        return url
    
    @property
    def timageURL(self):
        try:
            url = self.third_image.url
        except:
            url = ''
        return url

    
    @property
    def ftimageURL(self):
        try:
            url = self.fourth_image.url
        except:
            url = ''
        return url

class Comment(models.Model):
    post = models.ForeignKey(Blog,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.name

    


