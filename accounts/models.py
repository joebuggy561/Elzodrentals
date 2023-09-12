from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    #required fields

    def __str__(self):
        return self.name
    

# Create your models here.
