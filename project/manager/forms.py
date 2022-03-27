# Django Libs:
from django import forms
from .choices import FoodCategory
from .models import Food, Client, Circuit, DefaultCommand
from django.utils.safestring import mark_safe

			
class FoodForm(forms.Form):
	"""Surcharge the class Food to put place holder
	and remove help_text."""
	name = forms.Field(label="food_name"),
	price = forms.Field(label="food_price"),
	category = forms.Field(label="food_category"),



class ClientForm(forms.ModelForm):
	"""Surcharge the class Client to put place holder
	and remove help_text."""
	id = forms.Field(label="", widget=forms.TextInput(attrs={'class': 'invisible'}))
	first_name = forms.Field(label="", )
	last_name = forms.Field(label="", )
	address = forms.Field(label="", )
	circuit = forms.Field(label="", )
	default_command = forms.MultipleChoiceField(label="", choices=FoodCategory.choices, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}))
	#circuit = forms.MultipleChoiceField(label="", choices=Circuit.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}))

	class Meta():
		model = Client
		fields = ['id', 'first_name', 'last_name', 'address', 'default_command', 'circuit']
		widgets = {
		    'id': forms.TextInput(attrs={
		        'placeholder': 'Commande par défaut'}),
		    'default_command': forms.TextInput(attrs={
		        'placeholder': 'Commande par défaut'}),
		    'first_name': forms.TextInput(attrs={
		        'class': 'form_input',
		        'placeholder': 'Commande par défaut'}),
		    'last_name': forms.TextInput(attrs={
		        'class': 'form_input',
		        'placeholder': 'Commande par défaut'}),
		    'address': forms.TextInput(attrs={
		        'class': 'form_input',
		        'placeholder': 'Commande par défaut'}),
		}


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

			
class CommandForm(forms.Form):
	"""Surcharge the class Command to put place holder
	and remove help_text."""
	food = forms.Field(label=""),
	client = forms.Field(label=""),
	morning_command = forms.Field(label=""),
	evening_command = forms.Field(label=""),
	day_date_command = forms.Field(label=""),
	month_date__command = forms.Field(label=""),
	year_date__command = forms.Field(label=""),

			
class PlanningForm(forms.Form):
	"""Surcharge the class Planning to put place holder
	and remove help_text."""
	circuit = forms.Field(label=""),
	command = forms.Field(label=""),
