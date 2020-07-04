"""COVID19_BOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='voicebot Home Page'),
    path('covid19bot',views.covid19bot,name='Voice Bot Welcome Page'),
    path('voicebot',views.voicebot,name='Voice Bot Response Page'),
    path('aboutus',views.aboutus,name='About US'),
    path('contact',views.contact,name='Contact')
]
