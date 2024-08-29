from django.db import models




class Service(models.Model):
    title = models.CharField(max_length=250)
    descreption = models.TextField()
    form_link = models.URLField() 
    

    def __str__(self):
        return self.title
    



class Connect(models.Model):
    header  = models.CharField(max_length=250)
    image   = models.ImageField(upload_to='connect/photos') 
    content = models.TextField(blank=True, null=True)
    URL     = models.URLField()


    def __str__(self):
        return self.header