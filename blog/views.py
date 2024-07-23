
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sermon

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout



def home_page(request):
    return render(request, 'index.html')


def blogsPage(request):
    posts = Sermon.objects.all()
    return render(request, 'allblogs.html', {"posts":posts}) 

def page(request, id):
    post = get_object_or_404(Sermon, id=id)
    return render(request, 'page.html', {'post': post})


# def post_page(request, slug):
#     return HttpResponse(slug)
#     # return render(request, 'pages/post_detail.html' )

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form":form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blogs')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

    
def logout_user(request):
  if request.method == "POST":
    logout(request)
    return redirect('home')  # Redirect to home page after logout
  else:
    form = AuthenticationForm()
  return render(request, 'logout.html', {'form':form})


