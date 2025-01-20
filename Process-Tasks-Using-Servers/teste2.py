class Solution(object):
    def __init__(self):
        pass

    def empurrar(self, heap, elemento):
        heap.append(elemento)
        self.subirElemento(heap, len(heap) - 1)

    def retirar(self, heap):
        if len(heap) == 1:
            return heap.pop()
        menor = heap[0]
        heap[0] = heap.pop()
        self.descerElemento(heap, 0)
        return menor

    def subirElemento(self, heap, indice):
        pai = (indice - 1) // 2
        while indice > 0 and heap[indice][0] < heap[pai][0]:
            heap[indice], heap[pai] = heap[pai], heap[indice]
            indice = pai
            pai = (indice - 1) // 2

    def descerElemento(self, heap, indice):
        menor = indice
        esquerda = 2 * indice + 1
        direita = 2 * indice + 2

        if esquerda < len(heap) and heap[esquerda][0] < heap[menor][0]:
            menor = esquerda
        if direita < len(heap) and heap[direita][0] < heap[menor][0]:
            menor = direita

        if menor != indice:
            heap[indice], heap[menor] = heap[menor], heap[indice]
            self.descerElemento(heap, menor)

    def assignTasks(self, servidores, tarefas):

        servidores_livres = []
        servidores_ocupados = []


        for i, peso in enumerate(servidores):
            self.empurrar(servidores_livres, (peso, i))
        
        resposta = [0] * len(tarefas)
        tempo_atual = 0
        
        for i, tempo_tarefa in enumerate(tarefas):

            tempo_atual = max(tempo_atual, i)

            while servidores_ocupados and servidores_ocupados[0][0] <= tempo_atual:
                fim_livre, peso_srv, idx_srv = self.retirar(servidores_ocupados)
                self.empurrar(servidores_livres, (peso_srv, idx_srv))
            
            if not servidores_livres:
                fim_livre, peso_srv, idx_srv = self.retirar(servidores_ocupados)
                tempo_atual = fim_livre  

                while servidores_ocupados and servidores_ocupados[0][0] <= tempo_atual:
                    fim_livre2, peso_srv2, idx_srv2 = self.retirar(servidores_ocupados)
                    self.empurrar(servidores_livres, (peso_srv2, idx_srv2))
                
                resposta[i] = idx_srv
                novo_fim = tempo_atual + tempo_tarefa
                self.empurrar(servidores_ocupados, (novo_fim, peso_srv, idx_srv))
            else:
                peso_srv, idx_srv = self.retirar(servidores_livres)
                resposta[i] = idx_srv
                novo_fim = tempo_atual + tempo_tarefa
                self.empurrar(servidores_ocupados, (novo_fim, peso_srv, idx_srv))
        
        return resposta