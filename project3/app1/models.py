 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class test(models.Model):
    pr1=models.CharField(max_length=255)
    pr2=models.ImageField(upload_to="images/",null=True)

class customers(models.Model):
    user =models.OneToOneField(User,null=False,on_delete=models.CASCADE)    

    phone=models.CharField(max_length=255,blank=False)

    def __str__(self):
        return self.user.username



class Category(models.Model):
    category_name= models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)   
    price=models.FloatField(default=0.0)
    count=models.IntegerField(default=0)
    user_image=models.ImageField(upload_to="images/",null=True)

    def __str__(self):
      return self.name


class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)


    def __stt__(self):
        return f"{self.quantity} of {self.product.name}"


    def __stt__(self):
        return self.quantity * self.product.price


    def __stt__(self):
        return self.get_total_item_price()     


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)
    order_id=models.CharField(max_length=255,unique=True,default=None,blank=True,null=True)
    datetime_ofpayment=models.DateTimeField(auto_now_add=True)
    order_delivered=models.BooleanField(default=False)
    order_received=models.BooleanField(default=False)
    
              










