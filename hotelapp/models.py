from django.db import models

# Create your models here.
class Rooms(models.Model):
    id = models.BigAutoField(primary_key = True)
    floor = models.IntegerField(max_length = 3)
    name = models.CharField(max_length = 100)
    clean_status = models.CharField(max_length = 1)
    class Meta:
        db_table='Rooms'

class Reservations(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_ID = models.CharField(max_length=1000)
    room_ID = models.CharField(max_length=3)
    start_date = models.DateField()
    end_date = models.DateField()
    room_name = models.CharField(max_length=100, default='')
    class Meta:
        db_table='Reservations'

