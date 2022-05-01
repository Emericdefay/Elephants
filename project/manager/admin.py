# Django Libs:
from turtle import title
from django.contrib import admin
# Local Libs:
from .models import Food, DefaultCommand, Circuit, Client, Day, Month, Year, Command, WeekRange, Company


class CustomFood(admin.ModelAdmin):
	"""Allow to edit Food informations"""
	# list_display = ('', )
	fieldsets = [
		('price', {'fields': ['price']}),
		('category', {'fields': ['category']}),
	]


admin.site.register(Food, CustomFood)


class CustomCircuit(admin.ModelAdmin):
	"""Allow to edit Circuit informations"""
	# list_display = ('', )
	fieldsets = [
		('name', {'fields': ['name']}),
		# ('description_c', {'fields': ['description_c']}),
	]


admin.site.register(Circuit, CustomCircuit)


class CustomClient(admin.ModelAdmin):
	"""Allow to edit Client informations"""
	# list_display = ('', )
	fieldsets = [
		('first_name', {'fields': ['first_name']}),
		('last_name', {'fields': ['last_name']}),
		('address', {'fields': ['address']}),
		('postcode', {'fields': ['postcode']}),
		('address_details', {'fields': ['address_details']}),
		('cellphone', {'fields': ['cellphone']}),
		('cellphone2', {'fields': ['cellphone2']}),
		('order', {'fields': ['order']}),
		('circuit', {'fields': ['circuit']}),
		('client_command', {'fields': ['client_command']}),
	]


admin.site.register(Client, CustomClient)


class CustomCommand(admin.ModelAdmin):
	"""Allow to edit Command informations"""
	# list_display = ('', )
	fieldsets = [
		#('food', {'fields': ['food']}),
		('client', {'fields': ['client']}),
		('command_command', {'fields': ['command_command']}),
		('day_date_command', {'fields': ['day_date_command']}),
		('month_date_command', {'fields': ['month_date_command']}),
		('year_date_command', {'fields': ['year_date_command']}),
		('meals', {'fields': ['meals']}),
		('comment', {'fields': ['comment']}),
	]

admin.site.register(Command, CustomCommand)


class CustomCompany(admin.ModelAdmin):
	"""Allow to edit Company informations"""
	# list_display = ('', )
	fieldsets = [
		('comment_comp', {'fields': ['comment_comp']}),
		('cellphone_comp', {'fields': ['cellphone_comp']}),
		('company_comp', {'fields': ['company_comp']}),
		('address_comp', {'fields': ['address_comp']}),
		('siret_comp', {'fields': ['siret_comp']}),
	]

admin.site.register(Company, CustomCompany)
