from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("CustomerID", "CustomerName", "ContactName", "Address", "City", "PostalCode", "Country", "display_image",)
    search_fields = ["CustomerName__startswith"]
    list_filter = ["CustomerName"]   
    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url=obj.image.url, width=100, height=100,))
        else:
            return "No Image"
    display_image.short_description = 'image'
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("CategoryID", "CategoryName", "Description")
    search_fields = ["CategoryName__startswith"]
    list_filter = ["CategoryName"] 
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmployeeID', 'FirstName', 'LastName', 'BirthDate', 'display_image', 'Notes',)    
    search_fields = ["FirstName__startswith"]
    list_filter = ["FirstName"]
    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="50" height="50" />'.format(url=obj.image.url, width=100, height=100,))
        else:
            return "No Photo"
    display_image.short_description = 'image'
    
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('OrderDetailID', 'OrderID', 'ProductID', 'Quantity',)
    search_fields = ["OrderID__startswith"]
    list_filter = ["OrderID"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('OrderID', 'CustomerID', 'EmployeeID', 'OrderDate', 'ShipperID')
    search_fields = ["CustomerID__startswith"]
    list_filter = ["CustomerID"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductID', 'ProductName', 'SupplierID', 'CategoryID', 'Unit', 'Price', 'display_image', 'Description')
    search_fields = ["ProductName__startswith"]
    list_filter = ["ProductName"]
    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="50" height="50" />'.format(url=obj.image.url, width=100, height=100,))
        else:
            return "No Photo"
    display_image.short_description = 'image'
    
class ShipperAdmin(admin.ModelAdmin):
    list_display = ('ShipperID', 'ShipperName', 'Phone')
    search_fields = ["ShipperName__startswith"]
    list_filter = ["ShipperName"]
    
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('SupplierID', 'SupplierName', 'ContactName', 'Address', 'City', 'PostalCode', 'Country')
    search_fields = ["SupplierName__startswith"]
    list_filter = ["SupplierName"]
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Massage')
    search_fields = ["Name__startswith"]
    list_filter = ['Name']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product_id", "Name", "Email", "Review", "date")
    search_fields = ["product_id__startswith", "Name"]
    list_filter = ["product_id"]
    
    

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Review, ReviewAdmin)

class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...   
admin.site.register(Blog, BlogAdmin) 



