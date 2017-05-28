from django.shortcuts import render
from .models import memepostForm

def index(request):
    
    form = memepostForm(request.POST or None)
    
    if form.is_valid():
        print "valid"
        form.save()
    else:
        print "invalid"
    
    return render(request, 'memepost/post.html', {"form":form})