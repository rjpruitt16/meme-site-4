from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models

# Create your models here.
class memepost(models.Model):
    title = models.CharField(max_length = 140)
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
        
class memepostForm(ModelForm):
    class Meta:
        model = memepost
        fields = ["title", "model_pic", "date"]