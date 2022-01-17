import sys
sys.path.append('/mnt/c/Users/paulo/Desktop/EstudosAlura/API-Django/escola/')
sys.path.append('/home/paulo/Desktop/EstudosAlura/API-Django/escola/')
sys.path.append('/mnt/c/Users/paulo.campos/Desktop/EstudosAlura/API-Django/escola/')
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosEmUmCurso

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMAtriculaAlunos(generics.ListAPIView):
    """Listando as mátriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosEmUmCurso