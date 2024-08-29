from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.urls import reverse
import logging





def index(request):
    return render(request, 'blog/index.html')



def post(request, tag_slug=None):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    return render(request, 'blog/posts.html', {'posts': posts, 'tag':tag})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=slug, publish__year=year, publish__month=month,publish__day=day)
    post_url = request.build_absolute_uri(reverse('blog:post_detail', args=[year, month, day, slug]))

    return render(request, 'blog/post_detail.html', {'post':post, 'post_url':post_url})



def about(request):
    return render(request, 'blog/about.html')




logger = logging.getLogger(__name__)
def search(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = Post.objects.filter(status=Post.Status.PUBLISHED, title__icontains=query)
    except Exception as e:
        logger.error('Error during search: %s', e)

    return render(request, 'blog/search.html', context={'results':results, 'query':query})      