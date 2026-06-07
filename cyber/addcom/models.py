from django.db import models
class Addcom(models.Model):
    computer_id=models.IntegerField()
    computer_name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    model_no=models.CharField(max_length=50)
    series=models.CharField(max_length=50)
    ram=models.CharField(max_length=50)

# Create your models here.
