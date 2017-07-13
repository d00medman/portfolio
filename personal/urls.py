from django.conf.urls import url, include
from . import views
from django.views.generic import ListView
from personal.models import Language, Technology

q = Language.objects.all().prefetch_related('technology_set')

urlpatterns = [
    url(r'^$', views.index, name='index'), # Defining url patterns. As things stand, we have a start and an end
    url(r'^contact/', views.contact, name='contact'),
    url(r'^skills/$', ListView.as_view(queryset=q, template_name='personal/skills.html'))
]
