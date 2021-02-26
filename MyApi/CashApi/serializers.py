from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from CashApi.models import AccountHead, CashFlow

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
        "id",
        "username",
        "email",
        "password",
        )
        extra_kwargs = {
            "password": {
            "write_only": True, "style": {"input_type": "password"}
            },
            "email": {
            "write_only": True, "style": {"input_type": "email"}
            }
        }

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username =validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

# class JournalLogDetailSerializer(ModelSerializer):
#     class Meta:
#         model = JournalLogDetail
#         exclude = [
#         "amount"
#         ]

class CashSerializer(ModelSerializer):
    # asset = JournalLogDetailSerializer()
    # income = 0
    # expense = 0


    class Meta:
        model = CashFlow
        fields = (
        "time",
        "cash",
        )

    def create (self, validated_data):
        time = CashFlow.objects.time()
        cash = validated_data.pop("cash")
        cash.save()
        return cash
