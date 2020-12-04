from django.shortcuts import render
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.all()
        print(email)
    return render(request, 'order/orders_list.html',{'order_details': order_details})