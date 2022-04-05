# Django Libs:
from turtle import title
from django.contrib import admin
# Local Libs:
from .models import Food, DefaultCommand, Circuit, Client, Day, Month, Year, Command, WeekRange


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
	"""Allow to edit DefaultCommand informations"""
	# list_display = ('', )
	fieldsets = [
		('default', {'fields': ['default']}),
	]


admin.site.register(DefaultCommand, CustomDefaultCommand)


class CustomCircuit(admin.ModelAdmin):
	"""Allow to edit Circuit informations"""
	# list_display = ('', )
	fieldsets = [
		('name', {'fields': ['name']}),
		('description', {'fields': ['description']}),
	]


admin.site.register(Circuit, CustomCircuit)


class CustomClient(admin.ModelAdmin):
	"""Allow to edit Client informations"""
	# list_display = ('', )
	fieldsets = [
		('first_name', {'fields': ['first_name']}),
		('last_name', {'fields': ['last_name']}),
		('address', {'fields': ['address']}),
		('cellphone', {'fields': ['cellphone']}),
		('description', {'fields': ['description']}),
		('order', {'fields': ['order']}),
		('circuit', {'fields': ['circuit']}),
		('client_command', {'fields': ['client_command']}),
	]


admin.site.register(Client, CustomClient)


class CustomDay(admin.ModelAdmin):
	"""Allow to edit Month informations"""
	# list_display = ('', )
	fieldsets = [
		('date', {'fields': ['date']}),
	]


admin.site.register(Day, CustomDay)


class CustomMonth(admin.ModelAdmin):
	"""Allow to edit Year informations"""
	# list_display = ('', )
	fieldsets = [
		('date', {'fields': ['date']}),
	]


admin.site.register(Month, CustomMonth)


class CustomYear(admin.ModelAdmin):
	"""Allow to edit MorningNumberCommand informations"""
	# list_display = ('', )
	fieldsets = [
		('date', {'fields': ['date']}),
	]


admin.site.register(Year, CustomYear)


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

class CustomWeekRange(admin.ModelAdmin):
	"""Allow to edit Command informations"""
	# list_display = ('', )
	fieldsets = [
		('range', {'fields': ['range']}),
	]

admin.site.register(WeekRange, CustomWeekRange)
