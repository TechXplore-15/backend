from cardcontrol.models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CardSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

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


class TransactionsSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Transactions
        fields = [
            "id",
            "user_id",
            "transaction_date",
            "debit_account",
            "credit_account",
            "amount",
        ]

