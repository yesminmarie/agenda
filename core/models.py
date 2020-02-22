from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # máximo de 100 caracteres
    descricao = models.TextField(blank=True, null=True) # o campo não precisa ser preenchido
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #verbose_name customiza o nome
    data_criacao = models.DateTimeField(auto_now=True) #a uto_now vai automaticamente inserir a hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # cria uma chave estrangeira. Se o usuáriro for excluído da aplicação, exclui também todos os eventos dele


    # exige que a tabela chame "evento" ao invés de usar o padrão "core_evento"
    class Meta:
        db_table = 'evento'


    def __str__(self):
        return self.titulo

