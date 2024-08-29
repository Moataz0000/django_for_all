from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse




class Course(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250, unique=True)
    slug  = models.SlugField(unique=True)
    image = models.ImageField(upload_to='courses/images')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)
    link = models.URLField()


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)    

    def get_course_url(self):
        return reverse('courses:course_detail', args=[self.slug])  
