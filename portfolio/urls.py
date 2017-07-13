from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from portfolio.models import Project

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Project.objects.all().order_by('-id')[:25],
                                template_name='portfolio/portfolio.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Project,
                                             template_name='portfolio/project.html'))                            
]
