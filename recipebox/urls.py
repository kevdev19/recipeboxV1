"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from recipes.views import index_view, author_detail_view, recipe_detail_view, add_recipe, add_author


urlpatterns = [
    path('', index_view, name="recipes"),
    path('author/<int:author_id>/', author_detail_view),
    path('recipe/<int:recipe_id>/', recipe_detail_view),
    path('addrecipe/', add_recipe),
    path('addauthor/', add_author),
    path('admin/', admin.site.urls)
]
