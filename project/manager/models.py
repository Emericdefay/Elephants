from email.policy import default
from pydoc import describe
from statistics import mode
from django.db import models
from .choices import FoodCategory, CommandTimes

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.cache import cache


class Food(models.Model):
    """_summary_
    """
    category = models.CharField(verbose_name=('Plat'), max_length=200)
    price = models.CharField(verbose_name=("Prix"), max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.pk}: {self.category}"


@receiver(post_save, sender=Food)
def clear_cache(sender, instance, **kwargs):
    cache.clear()


class DefaultCommand(models.Model):
    default = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name=("Plats réguliers"), blank=False, null=False)
    order_food = models.IntegerField(verbose_name=("Position du plat"), default=0)

    def __str__(self):
        for name, member in FoodCategory.__members__.items():
            if member == self.default:
                return f"{self.pk} - {name}"
        return f"{self.id} - {self.default}"


class Circuit(models.Model):
    """_summary_
    """
    name = models.CharField(verbose_name=("Nom de la tournée"), max_length=200, blank=False, null=False)
    order_c = models.IntegerField(verbose_name=("Position de tournée"), default=0)
    circuit_color = models.CharField(verbose_name=("Couleur de tournée"), max_length=10, default="#ffffff")

    def __str__(self):
        return f"{self.pk}-{self.name}"


@receiver(post_save, sender=Circuit)
def clear_cache(sender, instance, **kwargs):
    cache.clear()


class Client(models.Model):
    """Modele client
    """
    create_datetime = models.DateTimeField(verbose_name=("Date de création"), auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name=("Date de mise à jour"), auto_now=True)
    first_name = models.CharField(verbose_name=("Prénom"), max_length=100, blank=False, null=False)
    last_name = models.CharField(verbose_name=("Nom"), max_length=100, blank=False, null=False)
    address = models.CharField(verbose_name=("Adresse"), max_length=200, blank=False, null=False)
    postcode = models.CharField(verbose_name=("00000 Ville"), max_length=100, blank=False, null=False)
    address_details = models.CharField(verbose_name=("Details"), max_length=200, blank=True, null=True)
    cellphone = models.CharField(verbose_name=("Telephone"), max_length=20, blank=True, null=True)
    cellphone2 = models.CharField(verbose_name=("Telephone secondaire"), max_length=20, blank=True, null=True)
    order = models.IntegerField(verbose_name=("Position de tournée"), default=0)
    client_command = models.ManyToManyField(DefaultCommand, related_name='command', blank=True)
    # TODO : models.SET(get_standart_circuit)
    circuit = models.ForeignKey(Circuit, on_delete=models.PROTECT)

    @property
    def has_comment(self):
        comments = [comment for comment in Command.objects.filter(client=self).values_list('comment', flat=True) if comment]
        return comments

    class Meta:
        ordering = ['circuit__order_c', 'last_name', 'first_name']
        # indexes = [models.Index(fields=['order',]),]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


@receiver(post_save, sender=Client)
def clear_cache(sender, instance, **kwargs):
    cache.clear()


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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # TODO : models.SET(get_standart_circuit)
    circuit = models.ForeignKey(Circuit, on_delete=models.PROTECT)
    command_command = models.IntegerField(verbose_name="", default=0)
    day_date_command = models.IntegerField(verbose_name="", blank=False)
    month_date_command = models.IntegerField(verbose_name="", blank=False)
    year_date_command = models.IntegerField(verbose_name="", blank=False)
    meals = models.ManyToManyField(DefaultCommand, related_name='meals', blank=True)
    comment = models.TextField(verbose_name="", blank=True, null=True)

    @property
    def is_different_from_default(self):
        return (list(self.meals.all().values_list('id', flat=True)) != list(self.client.client_command.all().values_list('id', flat=True)))

    @property
    def get_client(self):
        return self.client

    def __str__(self):
        return f"[{self.id}] {self.client.last_name} {self.client.first_name} : {self.day_date_command}/{self.month_date_command}/{self.year_date_command}"

    class Meta:
        indexes = [models.Index(fields=['day_date_command', 'month_date_command','year_date_command', 'client']),]


@receiver(post_save, sender=Command)
def clear_cache(sender, instance, **kwargs):
    cache.clear()


class Company(models.Model):
    """_summary_
    """
    comment_comp = models.TextField(verbose_name="Commentaire sous TTC", max_length=240, blank=True, null=True)
    cellphone_comp = models.TextField(verbose_name="Telephone Les Elephants", blank=True, null=True)
    company_comp = models.TextField(verbose_name="Nom de l'entreprise", blank=True, null=True)
    address_comp = models.TextField(verbose_name="Adresse de l'entreprise", blank=True, null=True)
    siret_comp = models.TextField(verbose_name="Numéro SIRET", blank=True, null=True)

    def __str__(self):
        return "Modèle de facture"


@receiver(post_save, sender=Company)
def clear_cache(sender, instance, **kwargs):
    cache.clear()


class WeekRange(models.Model):
    """"""
    range = models.IntegerField(verbose_name="", default=2)

    def __str__(self):
        return str(self.range)

@receiver(post_save, sender=WeekRange)
def clear_cache(sender, instance, **kwargs):
    cache.clear()