from enum import Enum
from django.db import models
from django.db.models import TextChoices


class FoodCategory(TextChoices, Enum):
    """_summary_
    """
    BREAD = ('0', "Pain")
    SOUP = ('1', "Soupe")
    BREAK = ('2', "Entrée")
    MEAL = ('3', "Plat")
    DESSERT = ('4', "Dessert")
    FRUIT = ('5', "Fruit")
    YOGOURT = ('6', "Yaourt")
    EK = ('7', "EK")
    FR = ('8', "FR")
    VEGETABLES = ('9', "Légumes")


class CommandTimes(TextChoices):
    NO = '0', ("Pas de commande") # default value
    YES = '1', ("Commande")
