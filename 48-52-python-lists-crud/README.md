# Aulas 48 a 52 - Listas em Python e Mutabilidade 📋

Nesta sequência de aulas explorei o tipo `list`. Diferente das strings, as listas são mutáveis, o que permite alterar, adicionar e remover elementos sem precisar criar um novo objeto na memória o tempo todo.
In these classes, I explored the `list` type. Unlike strings, lists are mutable, allowing elements to be changed, added, and removed without creating a new object in memory every time.

### :clipboard: O que aprendi / What I learned:

* **Conceito de CRUD:**
    * **Create:** `append` (final) e `insert` (qualquer posição).
    * **Read:** Acesso via índices `[i]`.
    * **Update:** Atribuição direta `lista[i] = novo_valor`.
    * **Delete:** `pop` (remove e retorna), `del` (apaga índice) e `clear` (limpa tudo).
* **Concatenação vs Extensão:** Entendi a diferença entre unir duas listas em uma terceira (`+`) e estender uma lista existente (`.extend()`).
* **Cuidado com a Memória:** Aprendi que ao fazer `lista_b = lista_a`, ambas apontam para o mesmo lugar. Se uma muda, a outra também muda. Para evitar isso, usamos o método `.copy()`.
* **Desempenho:** Entendi que remover ou inserir itens no **início** de listas grandes é custoso, pois o Python precisa reindexar todos os outros elementos.

---

### 🛠️ Métodos Principais / Key Methods:



| Método | Ação | Impacto |
| :--- | :--- | :--- |
| `.append(v)` | Adiciona `v` ao final. | Rápido (O(1)). |
| `.pop(i)` | Remove e retorna o item no índice `i`. | Rápido no final, lento no início. |
| `.insert(i, v)` | Insere `v` no índice `i`. | Lento (move todos os itens). |
| `.extend(list)` | Adiciona os itens de outra lista à atual. | Altera a lista original. |
| `.copy()` | Cria uma cópia rasa da lista. | Novo endereço de memória. |

---

### 💡 Insight:
As listas são como gavetas numeradas. Você pode trocar o que tem dentro da gaveta 2 sem precisar trocar o móvel inteiro. Porém, se você disser que a "gaveta do quarto" é a mesma que a "gaveta da sala" (`lista_a = lista_b`), qualquer meia que você colocar em uma aparecerá na outra!