from rest_framework import viewsets
from .models import Hudud, QurilishTashkiloti, QurilishBinolari
from .serializers import HududSerializer, QurilishTashkilotiSerializer, QurilishBinolariSerializer

class HududViewSet(viewsets.ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer

class QurilishTashkilotiViewSet(viewsets.ModelViewSet):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer

class QurilishBinolariViewSet(viewsets.ModelViewSet):
    queryset = QurilishBinolari.objects.all()
    serializer_class = QurilishBinolariSerializer
# 2-yoli--------------------------------------------------------------------------------
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hudud, QurilishTashkiloti, QurilishBinolari
from .serializers import HududSerializer, QurilishTashkilotiSerializer, QurilishBinolariSerializer
from .permissions import IsAdminOrReadOnly

class HududViewSet(viewsets.ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [IsAdminOrReadOnly]

class QurilishTashkilotiViewSet(viewsets.ModelViewSet):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer
    permission_classes = [IsAdminOrReadOnly]

class QurilishBinolariViewSet(viewsets.ModelViewSet):
    queryset = QurilishBinolari.objects.all()
    serializer_class = QurilishBinolariSerializer
    permission_classes = [IsAdminOrReadOnly]
