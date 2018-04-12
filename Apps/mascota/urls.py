from django.conf.urls import url
from Apps.mascota.views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]