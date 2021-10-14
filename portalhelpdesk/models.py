from django.db import models

# Create your models here.


class Dotaz(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Titul dotazu")

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return f'{self.nazev}'


class Poddotaz(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Titul poddotazu")
    dotaz = models.ManyToManyField(Dotaz)

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        nazev_2 = ','.join(str(v) for v in self.dotaz.all())
        return f'{self.nazev} ({nazev_2})'

