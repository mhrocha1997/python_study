class Programa:

    def __init__(self,nome,ano):
        self._nome=nome.title()
        self._ano=ano
        self._likes=0

    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self,novo_ano):
        self._ano = novo_ano

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}'
    
