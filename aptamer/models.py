from django.db import models

# Create your models here.


class Aptamer(models.Model):
    protein = models.CharField(max_length=2000)
    recommend_file = models.FileField()
    all_file = models.FileField()
    number_of_recommended = models.IntegerField()
    number_of_all = models.IntegerField()
    number_of_actual = models.IntegerField()

    def __str__(self):
        return self.protein
