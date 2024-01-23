from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import Booking, Menu

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {
            "no_of_guests" : {
                "min_value" : 1
            },
        }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        extra_kwargs = {
            "price" : {
                "min_value" : 1
            },
            "inventory" : {
                "min_value" : 0
            },
            "title" : {
                "validators" : [UniqueValidator(queryset=Menu.objects.all())]
            },
        }