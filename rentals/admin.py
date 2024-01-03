from django.contrib import admin


# Models
from .models import Rental, Payment
from motorcycles.models import Category, Motorcycle
from customers.models import Country, City, Customer


# Register your models here.
class CustomAdminSite(admin.AdminSite):
    site_header = "Motomami Rentals"
    site_title = "Motomami"


rental_admin_site = CustomAdminSite(name="MotoMamiAdmin")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "phone_number")


class CityAdmin(admin.ModelAdmin):
    list_display = ("__str__", "country_id")


class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "rental_rate")


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "customer", "amount", "payment_date")
    list_filter = ("payment_date", "customer", "rental")


class RentalAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "customer",
        "rental_date",
        "return_date",
        "active",
        "rental_pictures",
        "return_pictures",
    )

    list_filter = ("rental_date", "return_date")


# Rentals
rental_admin_site.register(Rental, RentalAdmin)
rental_admin_site.register(Payment, PaymentAdmin)

# Motorcycles
rental_admin_site.register(Category)
rental_admin_site.register(Motorcycle, MotorcycleAdmin)

# Customers
rental_admin_site.register(Country)
rental_admin_site.register(City, CityAdmin)
rental_admin_site.register(Customer, CustomerAdmin)
