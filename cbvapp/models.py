from django.db import models
from django.urls import reverse



# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    english='EG'
    kannada='KA'
    hindhi='HI'
    MEDIUM=[
        (english,'english'),
        (kannada,'kannada'),
        (hindhi,'hindi'),
    ]
    medium = models.CharField(max_length=100,default='English',choices=MEDIUM)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cbvapp:detail",kwargs={"pk":self.pk})
       
class Student(models.Model):
    std_name = models.CharField(max_length=100) 
    age = models.IntegerField()  
    marks = models.IntegerField()
    address = models.CharField(max_length=200) 
    school = models.ForeignKey(School,related_name='school',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.std_name
    
 

