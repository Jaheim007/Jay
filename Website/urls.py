from pydoc import visiblename
from django.urls import path
from Website import views

urlpatterns = [
    path('', views.index, name="Home"),
]