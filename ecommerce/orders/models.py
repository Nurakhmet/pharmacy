from django.db import models
from shop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator,MaxValueValidator
from coupons.models import Coupons


class order(models.Model):
	first_name 	= models.CharField(max_length=50)
	last_name	= models.CharField(max_length=50)
	email 		= models.EmailField()
	address 	= models.CharField(max_length=250)
	postal_code = models.CharField(max_length=50)
	city 		= models.CharField(max_length=100)
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	paid 		= models.BooleanField(default=False)
	coupon 		= models.ForeignKey(Coupons,related_name='orders',on_delete=models.CASCADE ,null=True,blank=True)
	discount 	= models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

	class Meta:
		ordering = ('-created',)
		verbose_name = "order"
		verbose_name_plural = "orders"

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		total_cost =  sum(item.get_cost() for item in self.items.all())
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order 		= models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
	product 	= models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
	price 		= models.DecimalField(max_digits=10,decimal_places=2)
	quantity	= models.PositiveIntegerField(default=1)

	class Meta:
		verbose_name = "OrderItem"
		verbose_name_plural = "OrderItems"


	def __str__(self):
		return '{}'.format(self.id)


	def get_cost(self):
		return self.price * self.quantity
