from rest_framework import serializers
from .models import MainProduct, Products

class MainProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = MainProduct
        fields = '__all__'

class ProductsSerializers(serializers.ModelSerializer):
    MainProduct = MainProductSerializers(read_only=True) 
    class Meta:
        model = Products
        fields = '__all__'
        
class SingleProductSerializer(serializers.ModelSerializer):
    MainProduct = MainProductSerializers(read_only=True) 
    class Meta:
        model = Products
        fields = '__all__'