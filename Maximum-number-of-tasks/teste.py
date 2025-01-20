class Solution(object):
    def maxTaskAssign(self, tarefas, trabalhadores, pilulas, forca_extra):

        tarefas.sort()
        trabalhadores.sort()
        
        def pode_atribuir(k):
            indice_tarefa = k - 1
            indice_trabalhador = len(trabalhadores) - 1
            pilulas_restantes = pilulas
            
            while indice_tarefa >= 0 and indice_trabalhador >= 0:
                if trabalhadores[indice_trabalhador] >= tarefas[indice_tarefa]:
                    indice_tarefa -= 1
                    indice_trabalhador -= 1
                else:
                    if pilulas_restantes > 0 and trabalhadores[indice_trabalhador] + forca_extra >= tarefas[indice_tarefa]:
                        pilulas_restantes -= 1
                        indice_tarefa -= 1
                        indice_trabalhador -= 1
                    else:
                        indice_trabalhador -= 1
            
            return indice_tarefa < 0
        
        baixo, alto = 0, len(tarefas)
        while baixo < alto:
            meio = (baixo + alto + 1) // 2
            if pode_atribuir(meio):
                baixo = meio
            else:
                alto = meio - 1
        
        return baixo
