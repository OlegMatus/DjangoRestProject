from rest_framework import serializers

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'price', 'size', 'day', 'created_at', 'updated_at')

        def validate_price(self, price):
            if price <= 0:
                raise serializers.ValidationError('Price must be greater than 0')
            return price

        def validate(self, attrs):
            price = attrs.get('price')
            size = attrs.get('size')

            if price == size:
                raise serializers.ValidationError('Price cannot be equal to size')

            return attrs
        # fields = '__all__'
# class PizzaSerializer(serializers.Serializer):
# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField(max_length=100)
# price = serializers.FloatField()
# size = serializers.CharField(max_length=20)
#
# created_at = serializers.DateTimeField(read_only=True)
# updated_at = serializers.DateTimeField(read_only=True)
#
# def create(self, validated_data: dict):
#     return PizzaModel.objects.create(**validated_data)
# def update(self, instance, validated_data: dict):
#     for k,v in validated_data.items():
#         setattr(instance,k,v)
#     instance.save()
#     return instance
