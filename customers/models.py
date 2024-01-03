from django.db import models

# Create your models here.


class Country(models.Model):
    """Country model

    Model to register the countries in which the company operates
    """

    country = models.CharField(max_length=50, unique=True, default="Australia")
    created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.country


class City(models.Model):
    """City model

    Model to register cities in which the company operates
    """

    country_id = models.ForeignKey(
        Country, on_delete=models.PROTECT, verbose_name="Country"
    )
    city = models.CharField(max_length=50, unique=True, default="Melbourne")
    created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ("-created",)

    def __str__(self):
        return self.city


class Customer(models.Model):
    """Customer model

    Model to register motorcycle occupants
    """

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50)
    city_id = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="City")
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    suburb = models.CharField(max_length=20)
    post_code = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20)
    customer_docs = models.FileField(
        upload_to="cust_docs/", null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name="Active")
    created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Customers"
        ordering = ("-created",)

    def __str__(self):
        return self.first_name + " " + self.last_name
