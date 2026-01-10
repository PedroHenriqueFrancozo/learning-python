# Aula 57 - Listas dentro de Listas (Matrizes) 📋

Nesta aula aprendi a trabalhar com estruturas de dados aninhadas. Entendi como acessar valores específicos usando múltiplos índices e como percorrer essas coleções usando laços de repetição aninhados.
In this class, I learned how to work with nested data structures. I understood how to access specific values using multiple indices and how to traverse these collections using nested loops.

### :clipboard: O que aprendi / What I learned:

* **Índices Bidimensionais:** Para acessar um item, usamos `lista[indice_da_lista_externa][indice_da_lista_interna]`. O primeiro colchete seleciona a "linha" e o segundo a "coluna".
* **Iteração Aninhada:** O primeiro `for` percorre as listas internas (as salas), e o segundo `for` percorre os itens dentro de cada uma dessas listas (os alunos).
* **Flexibilidade:** Listas aninhadas em Python não precisam ter o mesmo tamanho (diferente de matrizes rígidas em outras linguagens). Uma sala pode ter 2 alunos e a outra 10.
* **Modelagem de Dados:** Essa estrutura é a base para representar tabuleiros de jogos, tabelas de banco de dados e coordenadas.

---

### 🛠️ Visualização da Estrutura:



| Sala (Índice Externo) | Alunos (Índices Internos) |
| :---: | :--- |
| `salas[0]` | `[0] Maria, [1] Helena` |
| `salas[1]` | `[0] Elaine` |
| `salas[2]` | `[0] Luiz, [1] João, [2] Eduarda` |

---

### 💡 Insight:
Ao trabalhar com listas de listas, imagine sempre uma **árvore**. A lista principal é o tronco, as listas internas são os galhos e os elementos finais são as folhas. Para chegar na folha, você precisa obrigatoriamente passar pelo galho correto primeiro. Se tentar acessar um índice que não existe em uma das sublistas, o Python retornará o famoso `IndexError`.