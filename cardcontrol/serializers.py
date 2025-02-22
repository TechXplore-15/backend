from cardcontrol.models import *
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