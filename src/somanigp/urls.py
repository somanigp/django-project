"""
URL configuration for somanigp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from .views import home_page_view

# Routing patterns
urlpatterns = [
    path("", home_page_view),  # index or root page defined here.
    path("hellow-world/", home_page_view),
    # Routing any url path to any function 
    path("hellow-world.html", home_page_view),
    path('admin/', admin.site.urls),
]