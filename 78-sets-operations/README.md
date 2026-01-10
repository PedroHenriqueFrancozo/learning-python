# Aula 78 - Operações com Sets 🧮

Nesta etapa, aprendi como realizar operações matemáticas entre conjuntos. Essas ferramentas são extremamente eficientes para filtragem de dados e comparação de coleções.
In this stage, I learned how to perform mathematical operations between sets. These tools are extremely efficient for data filtering and collection comparison.

### :clipboard: Operações Principais / Main Operations:



[Image of Venn diagram showing union, intersection, and difference operations]


* **União (`|`):** Junta todos os elementos de ambos os sets (removendo as duplicatas). / Joins all elements from both sets (removing duplicates).
* **Interseção (`&`):** Retorna apenas os elementos que existem em **ambos** os conjuntos simultaneamente. / Returns only the elements that exist in both sets simultaneously.
* **Diferença (`-`):** Retorna os elementos que existem apenas no conjunto da esquerda. / Returns the elements that exist only in the left set.
* **Diferença Simétrica (`^`):** Retorna os elementos que são únicos para cada conjunto (o oposto da interseção). / Returns elements that are unique to each set (the opposite of intersection).

---

### 🛠️ Tabela de Operadores / Operators Table:

| Operação | Operador | Descrição |
| :--- | :--- | :--- |
| **Union** | `|` | Tudo de A e B. |
| **Intersection** | `&` | Apenas o que há em comum. |
| **Difference** | `-` | O que A tem que B não tem. |
| **Symmetric Diff**| `^` | O que é exclusivo de cada um. |

---

### 💡 Insight:
O uso de sets para essas operações é ordens de magnitude mais rápido do que tentar fazer o mesmo com listas usando `for` e `if`. Se você precisa comparar duas listas de milhares de e-mails para ver quais são novos, transforme-as em sets e use a **Diferença (`-`)**.