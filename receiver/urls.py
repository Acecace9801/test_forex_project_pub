from django.urls import path
from . import views


urlpatterns = [
    path('api/scanner/update/<str:name>', views.api_scanner_update_id, name='api_scanner_update_id'),
    path('api/scanner', views.api_scanner, name='api_scanner'),
    path('', views.index, name='index'),
    path('test/', views.test, name='test')
]