from django.db import models
import datetime
import os

def getFileName(request, filename):
    now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_filename='%s%s'%(now_time,filename)
    return os.path.join('uploads',new_filename)
# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=50, null=False, blank=True)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    role=models.CharField(max_length=100,null=False,blank=True)
    location=models.CharField(max_length=100,null=False,blank=True)
    discription=models.TextField(max_length=200,null=False,blank=True)
    phone=models.CharField(max_length=10,null=False,blank=True)
    email=models.EmailField(max_length=100,null=False,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    skill=models.CharField(max_length=100,null=False,blank=True)
    percentage=models.IntegerField(null=False,blank=True)
    
    def __str__(self):
        return self.skill

class Education(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    degree=models.CharField(max_length=100,null=False,blank=True)
    institue=models.CharField(max_length=100,null=False,blank=True)
    duration=models.CharField(max_length=100,null=False,blank=True)
    ed_discription=models.TextField(max_length=200,null=False,blank=True)
    
    def __str__(self):
        return self.degree
    
class Experience(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    e_role=models.CharField(max_length=100,null=False,blank=True)
    company=models.CharField(max_length=100,null=False,blank=True)
    e_duration=models.CharField(max_length=100,null=False,blank=True)
    e_discription=models.TextField(max_length=200,null=False,blank=True)
    
    def __str__(self):
        return self.e_role
    
class Project(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    p_image=models.ImageField(upload_to='project_img',null=False,blank=True)
    title=models.CharField(max_length=100,null=False,blank=True)
    p_discription=models.TextField(max_length=200,null=False,blank=True)
    
    def __str__(self):
        return self.title
    
class Certification(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    c_image=models.ImageField(upload_to='certification_img',null=False,blank=True)
    c_title=models.CharField(max_length=100,null=False,blank=True)
    c_discription=models.TextField(max_length=200,null=False,blank=True)
    
    def __str__(self):
        return self.c_title