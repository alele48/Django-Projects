"""kalgov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.contrib.auth import views

from kalgov.views import (HomePage,PublicSafetyPage,PublicWorkPage,
                         MarinePage,IdPage,RecreationPage,RecreationPage,
                         CustomPage)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',HomePage.as_view(),name='home'),
    re_path(r'', include('post.urls')),
    re_path(r'^accounts/login/$',views.LoginView.as_view(template_name="registration/login.html"),name='login'),
    re_path(r'^accounts/logout/$',views.LogoutView.as_view(),name='logout'),

    re_path(r'^public_safety/$',PublicSafetyPage.as_view(),name='safety'),
    re_path(r'^public_work/$',PublicWorkPage.as_view(),name='work'),
    re_path(r'^marine/$',MarinePage.as_view(),name='marine'),
    re_path(r'^recreation/$',RecreationPage.as_view(),name='recreation'),
    re_path(r'^id/$',IdPage.as_view(),name='id'),
    re_path(r'^custom/$',CustomPage.as_view(),name='custom'),
]
