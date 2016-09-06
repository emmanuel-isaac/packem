"""packem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from blueprints.user import views as user_views
from blueprints.cart import views as cart_views
from blueprints import api_root

router = routers.DefaultRouter()

urlpatterns = format_suffix_patterns([
    url(r'^api/$', api_root),
    url(r'^api/users/$', user_views.UserList.as_view(), name='user-list'),
    url(r'^api/carts/$', cart_views.CartList.as_view(), name='cart-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', user_views.UserDetail.as_view()),
    url(r'^api/carts/(?P<pk>[0-9]+)/$', cart_views.CartDetail.as_view(), name='cart-detail'),
])

urlpatterns += [
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
]
