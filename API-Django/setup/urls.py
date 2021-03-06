from django.contrib import admin
from django.db import router
from django.urls import path, include
from escola.views import AlunoViewSet, CursosViewSet, MatriculasViewSet, ListaMAtriculaAlunos, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename = 'Alunos')
router.register('cursos', CursosViewSet, basename = 'Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMAtriculaAlunos.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
