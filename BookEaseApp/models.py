from django.db import models

class Bus(models.Model):
    company_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} Bus from {self.origin} to {self.destination}"

class Flight(models.Model):
    airline_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.airline_name} Flight from {self.origin} to {self.destination}"
