from rest_framework import viewsets
from .models import  Provider, Product, Client, Command, Admin
from .serializers import (
    ProviderSerializer,
    ProductSerializer,
    ClientSerializer,
    CommandSerializer,
    AdminSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response



class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @action(methods=['get'], detail=False)
    def in_stock(self, request):
        products = Product.objects.filter(stock__gt=0).order_by('label')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def out_of_stock(self, request):
        products = Product.objects.filter(stock=0).order_by('label')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    @action(methods=['get'], detail=False)
    def get_product_by_provider(self, request):
        provider_id = request.query_params.get('provider_id')
        if provider_id:
            products = Product.objects.filter(provider__id=provider_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Provider ID not provided"}, status=400)
    @action(methods=['get'], detail=False)
    def get_product_by_price(self, request):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price and max_price:
            products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Price range not provided"}, status=400)    

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    @action(methods=['get'], detail=False)
    def get_client_by_email(self, request):
        email = request.query_params.get('email')
        if email:
            client = Client.objects.filter(email=email).first()
            if client:
                serializer = ClientSerializer(client)
                return Response(serializer.data)
            return Response({"error": "Client not found"}, status=404)
        return Response({"error": "Email not provided"}, status=400)
    @action(methods=['get'], detail=False)
    def get_client_by_type(self, request):
        type_client = request.query_params.get('typeClient')
        if type_client:
            clients = Client.objects.filter(typeClient=type_client)
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
        return Response({"error": "Type client not provided"}, status=400)

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    @action(methods=['get'], detail=False)
    def get_command_by_client(self, request):
        client_id = request.query_params.get('client_id')
        if client_id:
            commands = Command.objects.filter(client__id=client_id)
            serializer = CommandSerializer(commands, many=True)
            return Response(serializer.data)
        return Response({"error": "Client ID not provided"}, status=400)
    @action(methods=['get'], detail=False)
    def get_command_by_product(self, request):
        product_id = request.query_params.get('product_id')
        if product_id:
            commands = Command.objects.filter(product__id=product_id)
            serializer = CommandSerializer(commands, many=True)
            return Response(serializer.data)
        return Response({"error": "Product ID not provided"}, status=400)
    @action(methods=['get'], detail=False)
    def get_command_by_date(self, request):
        date_cmd = request.query_params.get('date_cmd')
        if date_cmd:
            commands = Command.objects.filter(date_cmd=date_cmd)
            serializer = CommandSerializer(commands, many=True)
            return Response(serializer.data)
        return Response({"error": "Date not provided"}, status=400)
    
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    @action(methods=['get'], detail=False)
    def get_admin_by_email(self, request):
        email = request.query_params.get('email')
        if email:
            admin = Admin.objects.filter(email=email).first()
            if admin:
                serializer = AdminSerializer(admin)
                return Response(serializer.data)
            return Response({"error": "Admin not found"}, status=404)
        return Response({"error": "Email not provided"}, status=400)








        