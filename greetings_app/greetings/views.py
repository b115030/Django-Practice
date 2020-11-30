from django.shortcuts import render
from .models import Post
from .forms import InputForm

# Create your views here.
def greeting_list(request):
    post = Post.objects.all()
    context = {
        'greeting_list': post
    }
    return render(request, "greetings/greeting_list.html", context)

def home_view(request):
    context = {}
    context['form']= InputForm() 
    return render(request, "greetings/greeting_list.html", context) 

def home(request):
    print(request.POST)
    return render(request, "greetings/greeting_list.html") 