from  rest_framework import serializers
from api.models import apimodel
class apiserializer(serializers.ModelSerializer):
    class Meta:
        model = apimodel
        fields = '__all__'
