from rest_framework import serializers
from .models import Provider, Product, Client, Command


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'password', 'email', 'phone', 'address']
        extra_kwargs = {
            'password': {'write_only': True},
        }

class ProductSerializer(serializers.ModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), required=False)
    provider_name = serializers.CharField(source='provider.name', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'label', 'price', 'stock', 'image', 'description', 'provider', 'provider_name']

class ClientSerializer(serializers.ModelSerializer):
    typeClient = serializers.CharField(source='get_typeClient_display', read_only=True)
    address = serializers.CharField(required=False)
    class Meta:
        model = Client
        fields = ['id', 'name', 'password', 'email', 'phone', 'address', 'familyName', 'typeClient']
        extra_kwargs = {
            'password': {'write_only': True},
        }

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ('id', 'client', 'product', 'quantity','date_cmd','amount')
        extra_kwargs = {
            'client': {'required': True},
            'product': {'required': True},
            'quantity': {'required': True},
        }  


class AdminSerializer(serializers.ModelSerializer):
    address = serializers.CharField(required=False)
    class Meta:
        model = Client
        fields = ['id', 'name', 'password', 'email', 'phone', 'address']
        extra_kwargs = {
            'password': {'write_only': True},
        }