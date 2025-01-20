# 1882. Process Tasks Using Servers
## Descrição

Você recebe dois arrays de inteiros indexados em 0, `servers` e `tasks`, de tamanhos \(n\) e \(m\), respectivamente:

- `servers[i]` é o peso do \(i\)-ésimo servidor.
- `tasks[j]` é o tempo necessário para processar a \(j\)-ésima tarefa em segundos.

As tarefas são atribuídas aos servidores usando uma fila de tarefas. Inicialmente, todos os servidores estão livres, e a fila está vazia.

### Regras de Processamento:

1. No segundo \(j\), a tarefa \(j\) é inserida na fila (a tarefa 0 é inserida no segundo 0).
2. Enquanto houver servidores livres e a fila não estiver vazia:
   - A tarefa no início da fila é atribuída ao servidor livre com o **menor peso**.
   - Em caso de empate no peso, é atribuída ao servidor com o **menor índice**.
3. Se não houver servidores livres e a fila não estiver vazia, aguardamos até que um servidor fique livre.
4. Se múltiplos servidores ficarem livres ao mesmo tempo, várias tarefas da fila serão atribuídas em ordem de inserção, seguindo as prioridades de peso e índice.

Um servidor que recebe a tarefa \(j\) no segundo \(t\) ficará livre novamente no segundo \(t + \text{tasks[j]}\).

Construa um array `ans` de tamanho \(m\), onde `ans[j]` é o índice do servidor que processará a \(j\)-ésima tarefa.

Retorne o array `ans`.

---

## Exemplos

### Exemplo 1:

**Entrada:**  
`servers = [3,3,2]`  
`tasks = [1,2,3,2,1,2]`  

**Saída:**  
`[2,2,0,2,1,2]`

**Explicação:**  

Eventos em ordem cronológica:
- No segundo 0, tarefa 0 é adicionada e processada pelo servidor 2 até o segundo 1.
- No segundo 1, o servidor 2 fica livre. A tarefa 1 é adicionada e processada pelo servidor 2 até o segundo 3.
- No segundo 2, a tarefa 2 é adicionada e processada pelo servidor 0 até o segundo 5.
- No segundo 3, o servidor 2 fica livre. A tarefa 3 é adicionada e processada pelo servidor 2 até o segundo 5.
- No segundo 4, a tarefa 4 é adicionada e processada pelo servidor 1 até o segundo 5.
- No segundo 5, todos os servidores ficam livres. A tarefa 5 é adicionada e processada pelo servidor 2 até o segundo 7.

---

### Exemplo 2:

**Entrada:**  
`servers = [5,1,4,3,2]`  
`tasks = [2,1,2,4,5,2,1]`  

**Saída:**  
`[1,4,1,4,1,3,2]`

**Explicação:**  

Eventos em ordem cronológica:
- No segundo 0, tarefa 0 é adicionada e processada pelo servidor 1 até o segundo 2.
- No segundo 1, tarefa 1 é adicionada e processada pelo servidor 4 até o segundo 2.
- No segundo 2, os servidores 1 e 4 ficam livres. A tarefa 2 é adicionada e processada pelo servidor 1 até o segundo 4.
- No segundo 3, a tarefa 3 é adicionada e processada pelo servidor 4 até o segundo 7.
- No segundo 4, o servidor 1 fica livre. A tarefa 4 é adicionada e processada pelo servidor 1 até o segundo 9.
- No segundo 5, a tarefa 5 é adicionada e processada pelo servidor 3 até o segundo 7.
- No segundo 6, a tarefa 6 é adicionada e processada pelo servidor 2 até o segundo 7.

---

## Restrições:

- \( \text{servers.length} = n \)  
- \( \text{tasks.length} = m \)  
- \( 1 \leq n, m \leq 2 \times 10^5 \)  
- \( 1 \leq \text{servers[i]}, \text{tasks[j]} \leq 2 \times 10^5 \)
