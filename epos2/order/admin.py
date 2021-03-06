from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product']}),
        ('Quantity', {'fields': ['quantity']}),
        ('Price', {'fields': ['price']}),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName','emailAddress', 'created', 'status']
    list_display_links = ('id', 'billingName', )
    search_fields = ['id', 'billingName', 'emailAddress','status'],
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName']
    editable_fields = ['status']
    fieldsets = [
        ('ORDER INFO', {'fields': ['id', 'token', 'total', 'created', 'status']}),
        ('BILLING INFO', {'fields': ['emailAddress','billingName']}),
    ]
    inlines = [
        OrderItemAdmin,
    ]
    def has_delete_permission(self, request, obj = None):
        return False
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj = OrderItem):
        return True
