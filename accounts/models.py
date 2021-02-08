from django.db import models


# Create your models here.
# in here we create classes that represent database tables
# we should import these model classes in admin.py
class Customer(models.Model):
    name = models.CharField(max_length=200,
                            null=True)  # we put null because sometimes there is no name so we dont want errors
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # in order to show the name instead of object(1) in django admin panel
        return self.name


# --------------------
class Tag(models.Model):                            # this class is used for many to many rel between
    name = models.CharField(max_length=200, null=True)  # products and order,sth like sports,summer,etc...


    def __str__(self):
        return self.name


# -----------------------------
class Product(models.Model):
    CATEGORY = (  # drop down menu for category
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)  # **
    description = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)  # *****

    def __str__(self):
        return self.name


# ----------------------------------------
class Order(models.Model):
    STATUS = (      # a drop down menu for status
        ('pending', 'pending'),
        ('out for delivery', 'out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  # very very important
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)  # we create the relationships in table

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)  # **
