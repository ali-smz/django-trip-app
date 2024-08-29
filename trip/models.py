from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

User = get_user_model()
# Create your models here.
class Trip(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name='trips')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    start_date = models.DateField(null=True , blank=True)
    end_date = models.DateField(null=True , blank=True)

    def __str__(self):
        return self.city
    

class Note(models.Model):
    EXURSIONS = (
        ('event' , 'Event'),
        ('dining' , 'Dining'),
        ('experience' , 'Experience'),
        ('general' , 'General'),
    )

    trip = models.ForeignKey(Trip , on_delete=models.CASCADE , related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100 , choices=EXURSIONS)
    img = models.ImageField(upload_to='notes' , blank=True , null=True)
    rating = models.PositiveSmallIntegerField(default=1 , validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} in {self.trip.city}"



