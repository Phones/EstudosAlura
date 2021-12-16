from django.contrib import admin
from escola.models import Aluno, Curso


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_files = ('nome',)
    list_por_page = 20


admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_link = ('id', 'codigo_curso')
    search_files = ('codigo_curso',)


admin.site.register(Curso, Cursos)