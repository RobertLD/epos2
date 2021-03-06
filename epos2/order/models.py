from django.db import models

# Create your models here.
class Order(models.Model):
    token = models.CharField(max_length = 250, blank = True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank = True)
    billingAddress = models.CharField(max_length=250, blank = True)
    status = models.CharField(max_length=250, default="In Progress", editable=True)

    class Meta:
        db_table = 'order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.CharField(max_length = 250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="USD Price")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table ='OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product
