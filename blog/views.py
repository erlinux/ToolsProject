from django.shortcuts import render

# Create your views here.

from .models import BlogArticles

# to reslove DoesNotExist at /blog/4/
from django.shortcuts import render,get_object_or_404

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request,article_id):
#   article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles,id=article_id)
    pub = article.published
    return render(request,"blog/content.html",{"article":article,"publish":pub})

