from django.db import models

# Create your models here.


class Aptamer(models.Model):
    protein = models.CharField(max_length=2000)
    recommend = models.CharField(max_length=5000)
    recommend_file = models.FileField()

    def __str__(self):
        return self.protein
