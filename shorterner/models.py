from django.db import models
from .utlis import code_generator,create_shortcode



class shorturl(models.Model):
    url=models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True,blank=True)



    def __str__(self):
        return self.url+ self.shortcode


    
    def save(self, *args,**kwargs):
        if self.shortcode== None or self.shortcode=='':
            self.shortcode=create_shortcode(self)
        super(shorturl,self).save(*args,**kwargs)



    



    
