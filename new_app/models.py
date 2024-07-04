from django.db import models

class Hudud(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class QurilishTashkiloti(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    qachon_tashkil_topgan = models.DateField()
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class QurilishBinolari(models.Model):
    qurilish_tashkiloti = models.ForeignKey(QurilishTashkiloti, on_delete=models.CASCADE)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    maydoni = models.FloatField()
    qavat = models.IntegerField()
    parkovka = models.BooleanField(default=False)
    bolalar_maydonchasi = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)

    def __str__(self):
        return self.name
