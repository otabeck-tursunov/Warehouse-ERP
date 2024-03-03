from django.db import models
from mainApp.models import *


class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    summa = models.FloatField(validators=[MinValueValidator(0)])
    tolandi = models.FloatField(validators=[MinValueValidator(0)])
    qarz = models.FloatField(default=0, validators=[MinValueValidator(0)])
    sana = models.DateField()
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.mahsulot} - {self.miqdor}"
