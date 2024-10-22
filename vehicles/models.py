from django.db import models
from django.core.validators import MinValueValidator


# to create a table in DB, install postgressql using ==> pip install psycopg2
class Vehicle(models.Model):

    COLORS = [
        ("black", "Black"),
        ("white", "White"),
        ("silver", "Silver"),
        ("gray", "Gray"),
        ("red", "Red"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("yellow", "Yellow"),
        ("brown", "Brown"),
        ("orange", "Orange"),
        ("purple", "Purple"),
        ("metallic_black", "Metallic Black"),
        ("metallic_silver", "Metallic Silver"),
        ("metallic_gray", "Metallic Gray"),
        ("metallic_red", "Metallic Red"),
        ("metallic_blue", "Metallic Blue"),
        ("metallic_green", "Metallic Green"),
        ("metallic_brown", "Metallic Brown"),
        ("pearl_white", "Pearl White"),
        ("matte_black", "Matte Black"),
        ("chrome", "Chrome"),
        ("gold", "Gold"),
        ("custom", "Custom Color"),
    ]

    ENGINE_TYPES = [
        ("petrol", "Petrol"),
        ("diesel", "Diesel"),
        ("electric", "Electric"),
    ]
    TRANSMISSION = [("manual", "Manual"), ("automatic", "Automatic")]
    FUEL_TYPES = [
        ("gasoline", "Gasoline"),
        ("diesel", "Diesel"),
        ("electric", "Electric"),
        ("hybrid", "Hybrid"),
        ("biodiesel", "Biodiesel"),
        ("hydrogen", "Hydrogen Fuel Cell"),
        ("ethanol", "Ethanol (Flex-Fuel)"),
    ]
    STATUS = [("active", "Active"), ("inactive", "Inactive"), ("sold", "Sold")]

    # Basic Information
    vin = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    manufacturer = models.CharField(max_length=50)  # Manufacturer (e.g., Toyota, Ford)
    year = models.IntegerField()  # Year of manufacture
    color = models.CharField(max_length=20, choices=COLORS)

    # Vehicle Specifications
    body_type = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50, choices=ENGINE_TYPES)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPES)
    seating_capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS)
    registration_date = models.DateField()

    class Meta:
        db_table = "vehicles"  # to force the naming of the table
