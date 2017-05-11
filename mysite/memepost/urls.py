from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from memepost.models import memepost

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=memepost.objects.all().order_by("-date")[:25],
                                    template_name="memepost/memepost.html")),
                                    
                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = memepost,
                                    template_name="memepost/picture.html")),

            ]