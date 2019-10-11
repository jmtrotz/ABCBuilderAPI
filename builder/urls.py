from django.conf.urls import url
from builder import views

urlpatterns = [
    url(r'^syncSource/$', views.syncSource),
    url(r'^buildROM/$', views.buildROM),
]
