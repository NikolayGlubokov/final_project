from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('', views.index, name='index'),
path('category/', views.category, name='category'),
path('parts/<int:schem_id>/', views.parts, name='parts'),
path('schemes/<int:cat_id>/', views.schemes, name='shemes'),
path('parts/journal/<int:part_id>', views.add, name='journal_add'),
]