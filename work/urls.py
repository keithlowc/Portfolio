"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from .views import redirect_to_site, show_site, capture_github, capture_linkedin, capture_instagram

urlpatterns = [
    path('', redirect_to_site, name='redirect_to_site'),
    path('home', show_site, name='show_site'),

    path('github', capture_github, name='capture_github'),
    path('linkedin', capture_linkedin, name='capture_linkedin'),
    path('instagram', capture_instagram, name='capture_instagram'),
]
