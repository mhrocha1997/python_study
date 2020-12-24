from filme import Filme
from serie import Serie
from playlist import Playlist

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em Pãnico', 1999,100)
demolidor = Serie('demolidor',2015,2)

demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fds = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fds)}')

for programa in playlist_fds:
    print(programa)
     