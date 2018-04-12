from django.conf.urls import url
from Apps.adopcion.views import index

urlpatterns = [
    url(r'^$', index),
]