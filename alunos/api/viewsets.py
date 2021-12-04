from rest_framework import viewsets
from .serializers import AlunoSerializers
from ..models import Aluno

class AlunoViewsets(viewsets.ModelViewSet):
    serializer_class = AlunoSerializers
    queryset = Aluno.objects.all()