from rest_framework import serializers

from .models import Order, Auto, Mark, Color


class OrderSerializer(serializers.ModelSerializer):
    mark = serializers.CharField(label='Марка', source='auto.mark', read_only=True)
    auto = serializers.SlugRelatedField(label='Модель', queryset=Auto.objects.all(), slug_field='model')
    color = serializers.SlugRelatedField(label='Цвет', queryset=Color.objects.all(), slug_field='color')

    class Meta:
        model = Order
        fields = '__all__'


class AutoSerializer(serializers.ModelSerializer):
    mark = serializers.SlugRelatedField(label='Марка', queryset=Mark.objects.all(), slug_field='mark')

    class Meta:
        model = Auto
        fields = '__all__'

    def create(self, validated_data):
        return super(AutoSerializer, self).create(validated_data)


class MarkSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField('get_auto_count')

    def get_auto_count(self, mark):
        """Считает количество автомобилей каждой марки"""
        if not mark.autos.all():
            return 0

        autos = mark.autos.all()
        mark_auto_count = []
        for auto in autos:
            mark_auto_count.append(sum([order.auto_count for order in auto.orders.all()]))
        return sum(mark_auto_count)

    class Meta:
        model = Mark
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField('get_auto_count')

    def get_auto_count(self, color):
        """Считает количество автомобилей с каждым цветом"""
        if not color.orders.filter(color=color):
            return 0
        return sum([order.auto_count for order in color.orders.filter(color=color)])

    class Meta:
        model = Color
        fields = '__all__'
