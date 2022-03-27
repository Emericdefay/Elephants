from email.policy import default
from statistics import mode
from django.db import models

from .choices import FoodCategory, CommandTimes


# Food
# -nom
# -prix
# -FoodCategory*
class Food(models.Model):
    """_summary_
    """
    name = models.CharField(verbose_name=("Nourriture"), max_length=100, blank=False, null=False)
    price = models.CharField(verbose_name=("Prix"), max_length=100, blank=False, null=False)
    category = models.CharField(max_length=2, choices=FoodCategory.choices, db_index=True)

    def __str__(self):
        print(FoodCategory(self.category).__dict__)
        return FoodCategory(self.category).label


class DefaultCommand(models.Model):
    default = models.CharField(max_length=10, choices=FoodCategory.choices, verbose_name=("Plats réguliers"), blank=False, null=False)

    def __str__(self):
        return str(self.default)


# Circuit
# -Name
# -Description
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


# Commande
# -Food*
# -Clients*
# -date_commande
# -
class Command(models.Model):
    """_summary_
    """
    food = models.ManyToManyField('Food', verbose_name=("Plat commandé"))
    client = models.ForeignKey(Client, verbose_name=("Client lié"), on_delete=models.CASCADE)
    morning_command = models.CharField(choices=CommandTimes.choices, max_length=2, verbose_name=("Commande Midi"))
    evening_command = models.CharField(choices=CommandTimes.choices, max_length=2, verbose_name=("Commande Soir"))
    day_date_command = models.IntegerField(verbose_name=("Jour"), blank=False, null=False)
    month_date_command = models.IntegerField(verbose_name=("Mois"), blank=False, null=False)
    year_date_command = models.IntegerField(verbose_name=("Année"), blank=False, null=False)
    
    def __str__(self):
        return f"{self.day_date_command}/{self.month_date_command}/{self.year_date_command} - {self.client}"


# Planning
# -Circuit*
# -Commande*
class Planning(models.Model):
    """_summary_
    """
    circuit = models.ForeignKey(Circuit, on_delete=models.PROTECT)
    command = models.ForeignKey(Command, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.circuit.name} : {self.command.day_date_command}/{self.command.month_date_command}/{self.command.year_date_command}"


