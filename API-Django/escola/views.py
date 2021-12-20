import sys
sys.path.append('/home/paulo/Desktop/EstudosAlura/API-Django/escola')
from django.db.models.query import QuerySet
from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

