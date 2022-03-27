# Django REST Libs:
from rest_framework import serializers
# Local Libs:
from .models import Food, DefaultCommand, Client, Circuit, Command, Planning


class FoodSerializer(serializers.ModelSerializer):
	"""
	Food serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Food
		fields = "__all__"


class DefaultCommandSerializer(serializers.ModelSerializer):
	"""
	DefaultCommand serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = DefaultCommand
		fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
	"""
	Client serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Client
		fields = "__all__"


class CircuitSerializer(serializers.ModelSerializer):
	"""
	Circuit serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Circuit
		fields = "__all__"


class CommandSerializer(serializers.ModelSerializer):
	"""
	Command serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Command
		fields = "__all__"


class PlanningSerializer(serializers.ModelSerializer):
	"""
	Planning serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Planning
		fields = "__all__"
