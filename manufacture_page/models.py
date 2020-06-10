from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Manu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(blank=True, max_length = 254)
    query = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
