
class Playlist:
    def __init__(self, nome, lista_programas):
        self.nome=nome
        self._programas = lista_programas

    def __getitem__(self,item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)