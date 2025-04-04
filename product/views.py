from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class MainProductView(APIView):
    def get(self, request):
        mainproduct = MainProduct.objects.all()
        serializer = MainProductSerializers(mainproduct, many=True)
        return Response(serializer.data)
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import ProductsSerializers

class ProductsView(APIView):
    def get(self, request, mainproduct):
        try:
            # Filter products by the slug of the MainProduct
            products = Products.objects.filter(MainProduct__slug=mainproduct)

            if not products.exists():
                return Response({"error": "Products not found"}, status=status.HTTP_302_FOUND)

            # Serialize the product queryset
            serializer = ProductsSerializers(products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Catch other unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleProductView(APIView):
    def get(self, request, slug):
        try:
            # Retrieve the single product by its slug
            product = Products.objects.filter(slug=slug).first()

            if not product:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            # Serialize the single product
            serializer = SingleProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Catch unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
