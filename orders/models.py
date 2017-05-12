from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon
from shop.models import Product
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    first_name = models.CharField(verbose_name=_('first_name'),
                    max_length=50)
    last_name = models.CharField(verbose_name=_('last_name'),
                    max_length=50)
    email = models.EmailField(verbose_name=_('email'))
    address = models.CharField(verbose_name=_('address'),
                    max_length=250)
    postal_code = models.CharField(verbose_name=_('postal_code'),
                    max_length=50)
    city = models.CharField(verbose_name=_('city'),
                    max_length=100)
    created = models.DateTimeField(verbose_name=_('created'),
                    auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'),
                    auto_now=True)
    paid = models.BooleanField(verbose_name=_('paid'), default=False)
    coupon = models.ForeignKey(Coupon, related_name='orders',
                            null=True, blank=True,
                            verbose_name=_('coupon'))
    discount = models.IntegerField(default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_('discount'))

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return _('Order')+'{}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',
                    verbose_name=_('order'))
    product = models.ForeignKey(Product, related_name='order_items',
                    verbose_name=_('product'))
    price = models.DecimalField(max_digits=10, decimal_places=2,
                    verbose_name=_('price'))
    quantity = models.PositiveIntegerField(default=1,
                    verbose_name=_('quantity'))

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
