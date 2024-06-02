from django.db import models

'''
    Id
    Livro
    Finalizado
    Resenha
    '''

class Livro(models.Model):
    Nome = models.TextField(max_length=100)
    Finalizado = models.BooleanField(default=False)
    Resenha = models.TextField(max_length=100)
    
    def is_finalizado(self):
        return "Sim" if self.Finalizado else "Não"
