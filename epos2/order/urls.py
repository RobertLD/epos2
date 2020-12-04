from django.urls import path, include
from . import views
app_name = 'order'
urlpatterns = [
    path('history/', views.orderHistory, name='order_history'),
    
]
