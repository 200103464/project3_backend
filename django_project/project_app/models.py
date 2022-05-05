from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name=("Date of birth"), blank=True, null=True)
    email = models.EmailField(blank=True, unique=True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=10)

    def str(self):
        return self.username
