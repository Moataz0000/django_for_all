from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250 , unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField(upload_to='blog/posts', blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    tags = TaggableManager()



    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]


    def __str__(self):
        return self.title
    
    def save(self, *args, **kewargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kewargs)    

    def get_post_url(self):
        return reverse('blog:post_detail', args=[ self.publish.year, self.publish.month, self.publish.day, self.slug])    
    
    def get_full_url(self):
        relative_url = self.get_post_url()
        return f"{settings.SITE_URL}{relative_url}"