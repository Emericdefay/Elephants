# Django Libs:
from logging import PlaceHolder
from django import forms
from .choices import FoodCategory
from .models import Food, Client, Circuit, DefaultCommand, Command, WeekRange, Company
from django.utils.safestring import mark_safe
from django.forms.models import BaseInlineFormSet
from django.forms.models import inlineformset_factory
from django.db import models
from . import models


			
class FoodForm(forms.ModelForm):
	"""Surcharge the class Food to put place holder
	and remove help_text."""
	category = forms.Field(label="Nom du plat", ),
	price = forms.Field(label="Prix", ),
	class Meta:
		model = Food
		fields = ['category', 'price']


class ClientForm(forms.ModelForm):
	"""Surcharge the class Client to put place holder
	and remove help_text."""
	first_name = forms.Field(label="Prénom", widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
	last_name = forms.Field(label="Nom", widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
	address = forms.Field(label="Adresse postale", widget=forms.TextInput(attrs={'placeholder': '5, Rue Salteur'}))
	postcode = forms.Field(label="00000 Ville", widget=forms.TextInput(attrs={'placeholder': '73000 Chambery'}))
	address_details = forms.Field(label="Détails", widget=forms.TextInput(attrs={'placeholder': 'Digicode, au troisième, Chez "un tel"'}))
	cellphone = forms.Field(label="Téléphone", widget=forms.TextInput(attrs={'placeholder': '0600000000'}))
	cellphone2 = forms.Field(label="Téléphone secondaire", widget=forms.TextInput(attrs={'placeholder': "De l'un de ses enfants?"}))
	circuit = forms.ModelChoiceField(label='Tournée',empty_label=None, queryset=Circuit.objects.all(), widget=forms.Select)

	class Meta:
		model = Client
		fields = [ 'first_name', 'last_name', 'address', 'postcode', 'address_details', 'cellphone', 'cellphone2', 'circuit']


class DefaultCommandForm(forms.ModelForm):
	"""_summary_

	Args:
		forms (_type_): _description_
	"""
	default = forms.Field(label="", )
	order_food = forms.Field(label="", )

	class Meta:
		model= DefaultCommand
		fields = ['default', 'order_food']


class CircuitForm(forms.ModelForm):
	"""Surcharge the class Circuit to put place holder
	and remove help_text."""
	name = forms.Field(label="Nom de la tournée", )

	class Meta:
		model = Circuit
		fields = ['name', ]


class CommandForm(forms.ModelForm):
	"""Surcharge the class Command to put place holder
	and remove help_text."""
	YEAR_CHOICES       = [(r, r) for r in range(2020, 2050)]
	MONTH_CHOICES      = [(r, r) for r in range(1, 13)]
	DAY_CHOICES        = [(r, r) for r in range(1, 32)]
	#food              = forms.Field(label="")
	command_command    = forms.IntegerField(label="", )
	meals              = forms.MultipleChoiceField(label="", choices=FoodCategory.choices, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}))
	comment            = forms.Field(label="", )
	day_date_command   = forms.DateField(label="", widget=forms.Select(choices=DAY_CHOICES)  )
	year_date_command  = forms.DateField(label="", widget=forms.Select(choices=YEAR_CHOICES) )
	month_date_command = forms.DateField(label="", widget=forms.Select(choices=MONTH_CHOICES))

	class Meta:
		model = Command
		fields = ['command_command', 'day_date_command','year_date_command', 'month_date_command', 'meals', 'comment' ]


class WeekRangeForm(forms.ModelForm):
	"""Surcharge the class Command to put place holder
	and remove help_text."""
	range = forms.IntegerField(label="", )

	class Meta:
		model = WeekRange
		fields = ['range', ]


# class CompanyForm(forms.ModelForm):
# 	"""
# 	Surcharge the class Company to put place holder
# 	and remove help_text.
# 	"""
# 	comment   = forms.Field(label="aa", )
# address   = forms.Field(label="zz", )
# company   = forms.Field(label="za", )
# siret     = forms.Field(label="vv", )
# cellphone = forms.Field(label="zz", )

# class Meta:
# 	model = Company
# 	fields = ['comment', 'cellphone', 'company', 'address', 'siret']
