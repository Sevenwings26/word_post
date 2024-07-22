
from django.shortcuts import render, get_object_or_404
from .models import Sermon
from django.http import HttpResponse

def home_page(request):
    posts = Sermon.objects.all()
    return render(request, 'index.html', {'posts': posts})

def page(request, id):
    post = get_object_or_404(Sermon, id=id)
    return render(request, 'page.html', {'post': post})


# def post_page(request, slug):
#     return HttpResponse(slug)
#     # return render(request, 'pages/post_detail.html' )
