from rest_framework import serializers
from .models import Hudud, QurilishTashkiloti, QurilishBinolari

class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'

class QurilishTashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishTashkiloti
        fields = '__all__'

class QurilishBinolariSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishBinolari
        fields = '__all__'
