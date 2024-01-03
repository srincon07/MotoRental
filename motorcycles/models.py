from django.db import models


# Create your models here.


class Category(models.Model):
    """Category model

    Model to register motorcycle categories
    """

    name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Motorcycle categories"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.name


class Motorcycle(models.Model):
    """Motorcycle model

    Model to record all motorcycles owned by the company
    """

    category = models.ManyToManyField(
        Category, related_name="categorys", verbose_name="Categories"
    )
    registration = models.CharField(max_length=10)
    registration_due = models.DateField(
        null=True, blank=True, verbose_name="Registration Due Date"
    )
    description = models.TextField(null=True, blank=True)
    year = models.PositiveSmallIntegerField()
    rental_rate = models.DecimalField(max_digits=7, decimal_places=2)
    insurance_policy = models.CharField(max_length=45)
    active = models.BooleanField(default=True, verbose_name="Active")
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Motorcycles"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.registration
