from django.urls import path

from . import views


app_name = "blog"
urlpatterns = [
    path('search/', views.search, name='search'),
    path('blog/<slug:slug>/', views.detail, name="detail"),
    path('category/<slug:slug>/', views.category_detail, name="category_detail"),
]