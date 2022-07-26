"""Jay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from Website import views
from Authentication import views as auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("register/", include("Website.urls")),
    path('', views.Homepage.as_view(), name="home"),
    path('about/', views.Aboutpage.as_view(), name="about"),
    path('shop_single/', views.Shopsingle.as_view(), name="shop_single"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('shop/', views.Shop.as_view(), name="shop"),
    path('connection/', auth.Connection.as_view(), name="connection"),
    path('register/', auth.Register.as_view(), name="register")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)