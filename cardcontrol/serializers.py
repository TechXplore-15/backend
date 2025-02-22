from cardcontrol.models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers



class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = [
            "id",
            "user_id",
            "subscriber_name",
            "subscriber_account",
            "pay_day",
            "is_subscribe",
            "end_date",
            "is_active"
        ]