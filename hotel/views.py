from rest_framework import viewsets
from .models import User, Order
from .serializers import UserSerializer, OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()
