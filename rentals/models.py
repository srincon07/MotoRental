# Django
from django.db import models

# Motorcycles
from motorcycles.models import Motorcycle

# Customers
from customers.models import Customer

# Create your models here.


class Rental(models.Model):
    """Rental model

    Model to register rental agreements
    """

    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name="Customer"
    )
    motorcycle = models.ForeignKey(
        Motorcycle, on_delete=models.PROTECT, verbose_name="Motorcycle"
    )
    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name="Active")
    rental_pictures = models.FileField(upload_to="rentals/")
    return_pictures = models.FileField(
        upload_to="returns/", null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Rentals"
        ordering = ("-created",)

    def __str__(self):
        return str(self.motorcycle)

    # @property
    # def rental_pic_url(self):
    #     return self.rental_pictures.url


class Payment(models.Model):
    """Payment model

    Model to register rental motorcycle payments
    """

    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name="Customer"
    )
    rental = models.ForeignKey(
        Rental, on_delete=models.PROTECT, verbose_name="Rental")
    amount = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Amount")
    payment_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Payments"
        ordering = ("-created",)

    def __str__(self) -> str:
        return str(self.rental)
