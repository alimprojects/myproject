import email
from pydoc import describe
from time import timezone
from typing import Self
from unicodedata import name
from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone


class Customer(models.Model):
    CustomerID = models.IntegerField()
    CustomerName = models.CharField(max_length=25)
    ContactName = models.CharField(max_length=25)
    Address = models.CharField(max_length=25)
    City = models.CharField(max_length=10)
    PostalCode = models.IntegerField()
    Country = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True, null=True)


    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
    image_tag.short_description = 'Image'
    
#import_export                            
class Blog(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    date_of_publishing = models.DateField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return self.title 
    
class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    Description = models.TextField()
    def __str__(self):
        return self.CategoryName
    
class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    BirthDate = models.DateField()
    image = models.ImageField(upload_to='image', blank=True)
    Notes = models.TextField(blank=True)   
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
    image_tag.short_description = 'image'
    
class OrderDetails(models.Model):
    OrderDetailID = models.AutoField(primary_key=True)
    OrderID = models.IntegerField()
    ProductID = models.IntegerField()
    Quantity = models.IntegerField()
    def __str__(self):
        return f"OrderDetailID: OrderID: {self.OrderID}, ProductID: {self.ProductID}, Quantity: {self.Quantity}"

class Order(models.Model):
    OrderID = models.IntegerField()
    CustomerID = models.IntegerField()
    EmployeeID = models.IntegerField()
    OrderDate = models.DateField()
    ShipperID = models.IntegerField()
    def __str__(self):
        return f"Order: CustomerID:{self.CustomerID}"
    
class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=50)
    SupplierID = models.IntegerField()
    CategoryID = models.IntegerField()
    Unit = models.CharField(max_length=50)
    Description = models.TextField(default='')
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image', blank=True)
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
    image_tag.short_description = 'image'
    
class Shipper(models.Model):
    ShipperID = models.AutoField(primary_key=True)
    ShipperName = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    def __str__(self):
        return self.ShipperName
    
class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=255)
    ContactName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=100)
    PostalCode = models.CharField(max_length=20)
    Country = models.CharField(max_length=100)
    def __str__(self):
        return self.SupplierName
    
class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(default="")
    Massage = models.TextField(default="")
    def __str__(self) :
        return self.Name
    
class Review(models.Model):
    product_id= models.IntegerField(default="")
    Name = models.CharField(max_length=30)
    Email = models.EmailField(default="")
    Review = models.TextField(default="")
    date = models.DateField(default=timezone.now)
    def __str__(self) :
        return f"Review for {self.Name}"
