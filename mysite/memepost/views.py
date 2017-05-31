from django.shortcuts import render
from .models import memepostForm
from django.http import HttpResponseRedirect

def index(request):
    
    form = memepostForm(request.POST, request.FILES)
    
    if request.method == "POST":
        if form.is_valid():
            print "VALID DAMN"
            newpost = form.save()
            return HttpResponseRedirect('/meme/')
        else:
            for i in form.errors.as_data().keys():
                print "\n Fucking error " + str(form.errors.as_data()[i])
    else:
        form = memepostForm()
        
    
    return render(request, 'memepost/post.html', {"form":form})