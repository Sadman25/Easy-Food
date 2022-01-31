from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields import DateField

# Create your models here.
class category (models.Model):
    category = models.CharField(max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.category

class product(models.Model):
    product_name= models.CharField(max_length=50, blank=False)
    product_description=models.CharField(max_length=500,null=False, blank=False)
    cover_photo=models.ImageField(null=False, blank=False)
    product_category = models.ForeignKey(category, null=True, on_delete= models.SET_NULL)
    product_price = models.PositiveIntegerField(null=False, blank=False)
    product_piece = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return 'Product: '+self.product_name 

    def get_absolute_url(self):
        return reverse('productDetails', kwargs={'pk':self.id})

class images(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    image=models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.product.product_name

class review (models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    review=models.TextField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    time=models.DateTimeField(auto_now_add=True,null=True)

class status(models.Model):
    status = models.CharField(max_length=50,default='Order Receieved')

    def __str__(self):
        return self.status

class order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    address=models.CharField(max_length=500)
    phone = models.CharField(max_length=15, default="")
    status=models.ForeignKey(status,on_delete=models.SET_NULL,null=True)
    order_time=models.DateTimeField(auto_now_add=True,null=True)
    update_time=models.DateTimeField(auto_now=True,null=True)
