from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from cardcontrol.models import *
from cardcontrol.serializers import *
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


class CardViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        user_id_received = request.query_params.get("user")
        # user_id_received = request.data["user"]
        print("user_id_received=",  request.query_params.get("user"))

        if not user_id_received:
            return Response(
                {"error": "User ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            user_id_int = int(user_id_received)
            cards = Card.objects.filter(user_id=user_id_int)
            print(cards)
            serializer = self.get_serializer(cards, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user_id = request.data.get("user")
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        card_id = request.data.get("card_id")
        if not card_id:
            return Response({"error": "Card ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            card = Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.data.get("user")
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                card.user = user
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if "card_name" in request.data:
            card.subscriber_name = request.data["card_name"]

        if "card_account" in request.data:
            card.subscriber_account = request.data["card_account"]

        if "end_date" in request.data:
            card.end_date = request.data["end_date"]

        if "pay_day" in request.data:
            card.end_date = request.data["pay_day"]

        if "is_subscribe" in request.data:
            card.end_date = request.data["is_subscribe"]

        if "is_active" in request.data:
            card.is_active = request.data["is_active"]
        card.save()
        serializer = self.get_serializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

