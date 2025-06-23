from rest_framework import generics
from .models import Tutorial
from .serializer import TutorialSerializer

# Create your views here.
class TutorialListView(generics.ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class TutorialDetailView(generics.RetrieveAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
