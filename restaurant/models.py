from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name + ": Rs " + str(self.price)

class Order(models.Model):
    product = models.ManyToManyField(Product)
    customer_name = models.CharField(max_length=200)
    order_placed = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.customer_name}'s Order"
