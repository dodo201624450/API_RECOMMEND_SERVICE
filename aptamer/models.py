from django.db import models

# Create your models here.

class Aptamer(models.Model):
    f_name = models.CharField(max_length=100)
    f_object = models.FileField()

    def __str__(self):
        return self.f_name
