class Solution(object):
    def maxTaskAssign(self, tarefas, trabalhadores, pilulas, forca_extra):
        tarefas.sort()
        trabalhadores.sort()
        
        indice_tarefa = 0
        indice_trabalhador = 0
        pilulas_usadas = 0
        tarefas_atribuidas = 0
        
        while indice_tarefa < len(tarefas) and indice_trabalhador < len(trabalhadores):
            if trabalhadores[indice_trabalhador] >= tarefas[indice_tarefa]:
                tarefas_atribuidas += 1
                indice_tarefa += 1
                indice_trabalhador += 1
            else:
                if pilulas_usadas < pilulas and trabalhadores[indice_trabalhador] + forca_extra >= tarefas[indice_tarefa]:
                    pilulas_usadas += 1
                    tarefas_atribuidas += 1
                    indice_tarefa += 1
                    indice_trabalhador += 1
                else:
                    indice_trabalhador += 1
                        
        return tarefas_atribuidas
