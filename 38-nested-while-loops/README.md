# Aula 38 - Laços de Repetição Aninhados (`while`) 📋

Nesta aula aprendi a estrutura de laços aninhados (*nested loops*). Essa técnica consiste em colocar um laço `while` dentro de outro, permitindo percorrer estruturas bidimensionais, como tabelas (linhas e colunas).
In this class, I learned about nested loops. This technique involves placing one `while` loop inside another, allowing for the traversal of two-dimensional structures, such as tables (rows and columns).

### :clipboard: O que aprendi / What I learned:

* **Lógica Interna vs. Externa:** O laço interno deve completar todas as suas repetições para cada única volta do laço externo.
* **Reinicialização de Variáveis:** A importância de resetar o contador do laço interno (`coluna = 1`) dentro do laço externo, caso contrário, ele não rodará novamente nas próximas linhas.
* **Complexidade:** Entendi que para cada "linha", o programa executa todas as "colunas". No exemplo de 5x5, o código dentro do laço interno roda 25 vezes.
* **Aplicações Práticas:** Essencial para gerar coordenadas, matrizes, tabuadas ou processar pixels em uma imagem.

---

### 🛠️ Visualização do Fluxo / Flow Visualization:



| Iteração Externa (Linha) | Iteração Interna (Coluna) | Total de Prints |
| :---: | :---: | :---: |
| Linha 1 | 1, 2, 3, 4, 5 | 5 |
| Linha 2 | 1, 2, 3, 4, 5 | 10 |
| ... | ... | ... |
| **Total Final** | | **25** |

---

### 💡 Insight:
Visualize os laços aninhados como os ponteiros de um relógio: o ponteiro dos segundos (laço interno) precisa dar uma volta completa de 60 segundos para que o ponteiro dos minutos (laço externo) avance apenas uma posição. É uma relação de dependência temporal e lógica.