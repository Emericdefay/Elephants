from email.policy import default
from pydoc import describe
from statistics import mode
from django.db import models
from .choices import FoodCategory, CommandTimes


class Food(models.Model):
    """_summary_
    """
    name = models.CharField(verbose_name=("Nourriture"), max_length=100, blank=False, null=False)
    price = models.CharField(verbose_name=("Prix"), max_length=100, blank=False, null=False)
    category = models.CharField(max_length=2, choices=FoodCategory.choices, db_index=True)

    def __str__(self):
        return FoodCategory(self.category).label


class DefaultCommand(models.Model):
    default = models.CharField(max_length=10, choices=FoodCategory.choices, verbose_name=("Plats réguliers"), blank=False, null=False)

    def __str__(self):
        for name, member in FoodCategory.__members__.items():
            if member == self.default:
                return name
        return self.default


class Circuit(models.Model):
    """_summary_
    """
    name = models.CharField(verbose_name=("Nom de la tournée"), max_length=200, blank=False, null=False)
    description = models.CharField(verbose_name=("Description de la tournée"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    """Modele client
    """
    create_datetime = models.DateTimeField(verbose_name=("Date de création"), auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name=("Date de mise à jour"), auto_now=True)
    first_name = models.CharField(verbose_name=("Prénom"), max_length=100, blank=False, null=False)
    last_name = models.CharField(verbose_name=("Nom"), max_length=100, blank=False, null=False)
    address = models.CharField(verbose_name=("Adresse"), max_length=1000, blank=False, null=False)
    default_command = models.ManyToManyField(DefaultCommand)
    circuit = models.ForeignKey(Circuit, on_delete=models.PROTECT)

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


class MorningNumberCommand(models.Model):
    """_summary_
    """
    number = models.IntegerField(verbose_name=("Nom"), blank=False, null=False)
    def __str__(self):
        return f"{self.number}"


class EveningNumberCommand(models.Model):
    """_summary_
    """
    number = models.IntegerField(verbose_name=("Nom"), blank=False, null=False)
    def __str__(self):
        return f"{self.number}"


class Command(models.Model):
    """_summary_
    """
    food = models.ManyToManyField('Food')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    morning_command = models.IntegerField(verbose_name="")
    evening_command = models.IntegerField(verbose_name="")
    day_date_command = models.IntegerField(verbose_name="", blank=False)
    month_date_command = models.IntegerField(verbose_name="", blank=False)
    year_date_command = models.IntegerField(verbose_name="", blank=False)

    def __str__(self):
        return f"{self.__dict__}"
