# 2071. Número máximo de tarefas que você pode atribuir
## Descrição

Você tem \(n\) tarefas e \(m\) trabalhadores. Cada tarefa tem um requisito de força armazenado em um array de inteiros indexados em 0, chamado `tasks`, em que a \(i\)-ésima tarefa exige `tasks[i]` de força para ser concluída. 

A força de cada trabalhador é armazenada em um array de inteiros indexados em 0, chamado `workers`, em que o \(j\)-ésimo trabalhador tem força `workers[j]`. 

- Cada trabalhador só pode ser atribuído a **uma única tarefa** e deve ter uma força maior ou igual ao requisito de força da tarefa, isto é:

  \[
  \text{`workers[j]`} \geq \text{`tasks[i]`}
  \]

- Além disso, você tem `pills` (**pílulas mágicas**) que aumentam a força de um trabalhador em `strength`. 
- Você pode decidir quais trabalhadores receberão essas pílulas mágicas, mas **cada trabalhador** pode receber **no máximo 1 pílula**.

Dado os arrays `tasks` e `workers`, e os inteiros `pills` e `strength`, retorne o **número máximo de tarefas** que podem ser concluídas.

---

*Entrada Exemplo:*

tasks = [3, 2, 1] workers = [0, 3, 3] pills = 1 strength = 1
