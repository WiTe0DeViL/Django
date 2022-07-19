from django.db import models

# Create your models here.


#class for Collections
class Collections(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')



#class for Products
class Product(models.Model):
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    Description = models.TextField()
    title = models.CharField(max_length=250)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collections, on_delete=models.PROTECT)


#class for Promotions
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)

    
# Class for Customer
class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    MEMBERSHIP_PLATINUM = "P"

    MEMBERSHIP_CHOISES = [
        (MEMBERSHIP_BRONZE, 'BRONZE'),
        (MEMBERSHIP_SILVER, 'SILVER'),
        (MEMBERSHIP_GOLD, 'GOLD'),
        (MEMBERSHIP_PLATINUM, 'PLATIONUM'),
    ]

    first_name = models.CharField(max_length=20)
<<<<<<< HEAD
<<<<<<< HEAD
    last_name = models.CharField(max_length=20)
<<<<<<< HEAD
    Email = models.EmailField(unique=True)
=======
    sunni = models.CharField(max_length=20)
=======
    last_name = models.CharField(max_length=20)
>>>>>>> parent of 0afe678 (update)
    email = models.EmailField(unique=True)
>>>>>>> parent of befa7f7 (update)
=======
    email = models.EmailField(unique=True)
>>>>>>> parent of 7eb07a7 (update)
    phone = models.CharField(max_length=25)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOISES, default=MEMBERSHIP_SILVER)
    



# Class for Orders
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'PENDING'),
        (PAYMENT_STATUS_COMPLETE, 'COMPLETE'),
        (PAYMENT_STATUS_FAILED, 'FAILED'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


# Class for Adress (with OneToOne--> relationship with the Customer)
class Address(models.Model):
    door_num = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
        )
    
# Class For orderItems
class orderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product= models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

# Class For Cart
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now=True)


# Class For cartItems
class cartItems(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
