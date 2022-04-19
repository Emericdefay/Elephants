from email.policy import default
from pydoc import describe
from statistics import mode
from django.db import models
from .choices import FoodCategory, CommandTimes


class Food(models.Model):
    """_summary_
    """
    category = models.CharField(verbose_name=('Catégorie'), max_length=200)
    price = models.CharField(verbose_name=("Prix"), max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.pk}: {self.category}"


class DefaultCommand(models.Model):
    default = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name=("Plats réguliers"), blank=False, null=False)

    def __str__(self):
        for name, member in FoodCategory.__members__.items():
            if member == self.default:
                return f"{self.pk} - {name}"
        return f"{self.id} - {self.default}"


class Circuit(models.Model):
    """_summary_
    """
    name = models.CharField(verbose_name=("Nom de la tournée"), max_length=200, blank=False, null=False)
    description_c = models.CharField(verbose_name=("Description de la tournée"), max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.pk}-{self.name}"


class Client(models.Model):
    """Modele client
    """
    create_datetime = models.DateTimeField(verbose_name=("Date de création"), auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name=("Date de mise à jour"), auto_now=True)
    first_name = models.CharField(verbose_name=("Prénom"), max_length=100, blank=False, null=False)
    last_name = models.CharField(verbose_name=("Nom"), max_length=100, blank=False, null=False)
    address = models.CharField(verbose_name=("Adresse"), max_length=1000, blank=False, null=False)
    postcode = models.CharField(verbose_name=("00000 Ville"), max_length=1000, blank=False, null=False)
    cellphone = models.CharField(verbose_name=("Telephone"), max_length=20, blank=True, null=True)
    description = models.TextField(verbose_name=("Description"), max_length=1000, blank=True, null=True)
    order =models.IntegerField(verbose_name=("Position de tournée"), default=0)
    client_command = models.ManyToManyField(DefaultCommand, related_name='command', blank=True)
    circuit = models.ForeignKey(Circuit, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['circuit', 'last_name', 'first_name']
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Day(models.Model):
    """_summary_
    """
    date = models.IntegerField(verbose_name=("Jour"), blank=False, null=False)
    def __str__(self):
        return f"{self.date}"


class Month(models.Model):
    """_summary_
    """
    date = models.IntegerField(verbose_name=("Mois"), blank=False, null=False)
    def __str__(self):
        return f"{self.date}"


class Year(models.Model):
    """_summary_
    """
    date = models.IntegerField(verbose_name=("Année"), blank=False, null=False)
    def __str__(self):
        return f"{self.date}"


class Command(models.Model):
    """_summary_
    """
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    circuit = models.ForeignKey(Circuit, on_delete=models.DO_NOTHING)
    command_command = models.IntegerField(verbose_name="", default=0)
    day_date_command = models.IntegerField(verbose_name="", blank=False)
    month_date_command = models.IntegerField(verbose_name="", blank=False)
    year_date_command = models.IntegerField(verbose_name="", blank=False)
    meals = models.ManyToManyField(DefaultCommand, related_name='meals', blank=True)
    comment = models.TextField(verbose_name="", blank=True, null=True)
    reduction = models.FloatField(verbose_name="", blank=True, null=True)
    free = models.BooleanField(verbose_name="", blank=True, null=True)
    def __str__(self):
        return f"{self.client.last_name} {self.client.first_name} : {self.day_date_command}/{self.month_date_command}/{self.year_date_command}"


class WeekRange(models.Model):
    """"""
    range = models.IntegerField(verbose_name="", default=2)

    def __str__(self):
        return str(self.range)
