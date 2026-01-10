# Aula 78 - Introdução aos Sets (`set`) 📐

Nesta aula aprendi os fundamentos dos conjuntos em Python, uma estrutura inspirada diretamente na teoria dos conjuntos matemática. O uso de sets é a forma mais eficiente de garantir que uma coleção não possua elementos repetidos.
In this class, I learned the fundamentals of sets in Python, a structure directly inspired by mathematical set theory. Using sets is the most efficient way to ensure a collection has no repeating elements.

### :clipboard: O que aprendi / What I learned:

* **Representação Visual:** Entendi que o comportamento dos sets segue o **Diagrama de Venn**.
* **Unicidade e Imutabilidade:** Valores duplicados são ignorados e apenas tipos imutáveis (como `str`, `int`, `tuple`) podem ser armazenados.
* **Métodos de Manipulação:**
    * `add`: Adiciona um único item.
    * `update`: Adiciona vários itens (precisa de um iterável).
    * `discard`: Remove um item de forma segura.
* **Operadores Matemáticos:** O Python oferece símbolos intuitivos para operações de união (`|`), intersecção (`&`) e diferença (`-` e `^`).

---

### 🛠️ Métodos e Operadores / Methods and Operators:



| Ferramenta | Ação |
| :--- | :--- |
| `set()` | Cria um conjunto vazio. |
| `add()` | Insere um valor. |
| `update()` | Insere múltiplos valores. |
| `discard()` | Remove um valor sem gerar erro. |

---

### 💡 Insight:
Uma curiosidade importante: em Python, para criar um dicionário vazio usamos `variavel = {}`. Para criar um **set vazio**, somos obrigados a usar `variavel = set()`, pois as chaves vazias já estão "reservadas" para os dicionários.