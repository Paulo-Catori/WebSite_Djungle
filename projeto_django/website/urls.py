"""
URL configuration for website project.

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
#from django.contrib import admin
from django.urls import path
from design_limitada import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.design_limitada_index, name="index"),
    path("elementos de design/", views.design_limitada_elementos_de_design, name="elementos de design"),
    path("/""/contatos", views.design_limitada_contatos, name="contatos"),
]
