from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalendarioView.as_view(), name='calendario'),
    path('compras/', views.compras, name='compras'),
    path('<int:pk>/info/', views.detail, name='info')
]