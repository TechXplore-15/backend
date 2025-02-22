from django.contrib import admin
from cardcontrol.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subscriber_name",
        "subscriber_account",
        "pay_day",
        "is_subscribe",
        "end_date",
        "is_active",
        "created",
    )
    search_fields = ("subscriber_name", "subscriber_account")
    list_filter = ("is_subscribe", "is_active")
    ordering = ("-created",)
