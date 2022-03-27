# Django Libs:
from django.contrib import admin
# Local Libs:
from .models import Food, Client, Circuit, Command, Planning, DefaultCommand


class CustomFood(admin.ModelAdmin):
	"""Allow to edit Food informations"""
	# list_display = ('', )
	fieldsets = [
		('name', {'fields': ['name']}),
		('price', {'fields': ['price']}),
		('category', {'fields': ['category']}),
	]

admin.site.register(Food, CustomFood)

class CustomDefaultCommand(admin.ModelAdmin):
	""""""
	# list_display = ('', )
	fieldsets = [
		('default', {'fields': ['default']}),
	]

admin.site.register(DefaultCommand, CustomDefaultCommand)



class CustomClient(admin.ModelAdmin):
	"""Allow to edit Client informations"""
	# list_display = ('', )
	fieldsets = [
		('first_name', {'fields': ['first_name']}),
		('last_name', {'fields': ['last_name']}),
		('address', {'fields': ['address']}),
		('default_command', {'fields': ['default_command']}),
		('circuit', {'fields': ['circuit']}),
	]


admin.site.register(Client, CustomClient)


class CustomCircuit(admin.ModelAdmin):
	"""Allow to edit Circuit informations"""
	# list_display = ('', )
	fieldsets = [
		('name', {'fields': ['name']}),
		('description', {'fields': ['description']}),
	]


admin.site.register(Circuit, CustomCircuit)


class CustomCommand(admin.ModelAdmin):
	"""Allow to edit Command informations"""
	# list_display = ('', )
	fieldsets = [
		('food', {'fields': ['food']}),
		('client', {'fields': ['client']}),
		('morning_command', {'fields': ['morning_command']}),
		('evening_command', {'fields': ['evening_command']}),
		('day_date_command', {'fields': ['day_date_command']}),
		('month_date_command', {'fields': ['month_date_command']}),
		('year_date_command', {'fields': ['year_date_command']}),
	]


admin.site.register(Command, CustomCommand)


class CustomPlanning(admin.ModelAdmin):
	"""Allow to edit Planning informations"""
	# list_display = ('', )
	fieldsets = [
		('circuit', {'fields': ['circuit']}),
		('command', {'fields': ['command']}),
	]


admin.site.register(Planning, CustomPlanning)
