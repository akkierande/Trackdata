from django.conf.urls import url,include
from . import views
from .views import Image_View,Checkout


urlpatterns = [
    url(r'^$',views.index,name='index'),
    #Project/1/
    url(r'^(?P<project_id>[0-9]+)/$',views.detail,name='Detail'),
    url(r'^(?P<package_id>[0-9]+)/$',views.detail,name='Package'),
    url(r'^userprofile/$', views.userprofile, name='profile'),
    url(r'^images/$', Image_View.as_view(), name='Images'),
    url(r'^images/(?P<pk>\d+)/$', views.image_edit, name='image_edit'),
    #url(r'^checkout/(?P<pk>\d+)/$', views.Checkout, name='Checkout'),
    #url(r'^checkout/$', Checkout.as_view(), name='Checkout'),

    url(r'^checkout/$', Checkout.as_view(), name='Checkout'),
    #url(r'^packages/delete/(?P<pk>\d+)/$', views.package_delete, name='package_delete'),
]