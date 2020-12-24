from funcionario import Funcionario
from alura import Alura
from caelum import Caelum
from junior import Junior
from pleno import Pleno
from senior import Senior

jose = Junior('José')
jose.busca_perguntas_sem_respostas()

luan = Pleno('Luan')
luan.busca_perguntas_sem_respostas()
luan.busca_cursos_do_mes

luan.mostrar_tarefas()

luan = Senior('Luan')
print(luan)