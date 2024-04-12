from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(), name='menu-list'),
    path('<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail'),
]
