from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = "givesmartapp"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^search/', views.search, name='search'),
    url(r'^compare/', views.compare, name='compare'),
    url(r'^charity/(?P<name>[\w]+)/$', views.view_charity, name='viewcharity'),
    url(r'^donate/', views.donate, name='donate'),
    url(r'^submit/', views.submit_donation, name='donation_submission'),
    url(r'^$', views.index, name='index'),
]