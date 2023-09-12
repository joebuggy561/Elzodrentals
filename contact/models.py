from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
