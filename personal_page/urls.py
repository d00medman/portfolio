from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index') # Defining url patterns. As things stand, we have a start and an end
]
