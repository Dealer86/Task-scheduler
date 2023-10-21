from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('task/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.task_update, name='update'),
    path('export-csv/', views.export_csv, name='export-csv'),
    path('about/', views.about, name='about'),
]
