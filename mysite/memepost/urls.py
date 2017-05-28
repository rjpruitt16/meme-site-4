from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from memepost.models import memepost, memepostForm
from . import views

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=memepost.objects.all().order_by("-date")[:25],
                                    template_name="memepost/memepost.html")),
                                    
                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = memepost,
                                    template_name="memepost/picture.html")),

                url(r'^post/', views.index, name="index")
            ]