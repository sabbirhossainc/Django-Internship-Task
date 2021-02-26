from rest_framework.viewsets import ModelViewSet
from CashApi.models import AccountHead, CashFlow
from django.contrib.auth.models import User
from CashApi.serializers import CreateUserSerializer, CashSerializer

# Create your views here.

class CreateUserViewsets(ModelViewSet):
    serializer_class= CreateUserSerializer
    queryset = User.objects.all()

class CashViewSet(ModelViewSet):
    serializer_class= CashSerializer
    queryset = CashFlow.objects.all()
