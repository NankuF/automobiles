from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Order, Auto, Mark, Color
from .serializers import AutoSerializer, MarkSerializer, ColorSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('auto__mark',)
    search_fields = ('color__color',)
    ordering_fields = ('auto_count',)


class AutoViewSet(viewsets.ModelViewSet):
    serializer_class = AutoSerializer
    queryset = Auto.objects.all()


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
