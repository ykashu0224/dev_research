from rest_framework.viewsets import ModelViewSet
from .models import Hello
from .serializers import HelloSerializer

# Create your views here.\
class HelloViewSet(ModelViewSet):
    
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer

