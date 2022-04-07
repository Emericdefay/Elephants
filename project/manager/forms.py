# Django Libs:
from django import forms
from .choices import FoodCategory
from .models import Food, Client, Circuit, DefaultCommand, Command, WeekRange
from django.utils.safestring import mark_safe
from django.forms.models import BaseInlineFormSet
from django.forms.models import inlineformset_factory
from django.db import models



			
class FoodForm(forms.Form):
	"""Surcharge the class Food to put place holder
	and remove help_text."""
	price = forms.Field(label="food_price"),
	category = forms.Field(label="food_category"),


class ClientForm(forms.ModelForm):
	"""Surcharge the class Client to put place holder
	and remove help_text."""
	first_name = forms.Field(label="Prénom", )
	last_name = forms.Field(label="Nom", )
	address = forms.Field(label="Adresse postale", )
	cellphone = forms.Field(label="Téléphone", )
	description = forms.Field(label="Description", )
	circuit = forms.ModelChoiceField(label='Tournée',empty_label=None, queryset=Circuit.objects.all(), widget=forms.Select)
	#client_command = forms.MultipleChoiceField(label="Commande générale", choices=Circuit.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}))
	#circuit = forms.MultipleChoiceField(label="", choices=Circuit.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}))

	class Meta:
		model = Client
		fields = [ 'first_name', 'last_name', 'address', 'cellphone', 'description', 'circuit']


class DefaultCommandForm(forms.ModelForm):
	"""_summary_

	Args:
		forms (_type_): _description_
	"""
	default = forms.Field(label="", )

	class Meta:
		model= DefaultCommand
		fields = ['default']

			
class CircuitForm(forms.ModelForm):
	"""Surcharge the class Circuit to put place holder
	and remove help_text."""
	id = forms.Field(label="", widget=forms.TextInput(attrs={'class': 'invisible'}))
	name = forms.Field(label="", )

	class Meta:
		model = Circuit
		fields = ['id', 'name']


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
	reduction          = forms.FloatField(label="",)
	free               = forms.BooleanField(label="")

	class Meta:
		model = Command
		fields = ['command_command', 'day_date_command','year_date_command', 'month_date_command', 'meals', 'comment' ]


class WeekRangeForm(forms.ModelForm):
	"""Surcharge the class Command to put place holder
	and remove help_text."""
	range    = forms.IntegerField(label="", )

	class Meta:
		model = WeekRange
		fields = ['range', ]
