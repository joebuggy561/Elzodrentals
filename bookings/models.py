from django.db import models



class Bookings(models.Model):
    p_location = models.CharField(max_length=50)
    d_location = models.CharField(max_length=50)
    p_date = models.TextField()
    d_date = models.TextField()
    p_up_time = models.TextField()

    class Meta:
        verbose_name = 'bookings'
        verbose_name_plural = 'bookings'


    def __str__(self):
        return self.p_location

# Create your models here.
