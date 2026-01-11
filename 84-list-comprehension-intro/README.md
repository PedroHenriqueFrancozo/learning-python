# Aula 84 - Introdução à List Comprehension ⚡

Nesta aula, aprendi a utilizar a **List Comprehension**, uma sintaxe curta que permite criar novas listas a partir de iteráveis em apenas uma linha de código.

### :clipboard: O que aprendi:

* **Sintaxe Básica:** A estrutura segue o padrão `[expressão for item in iterável]`.
* **Transformação de Dados:** Posso aplicar operações matemáticas ou manipular strings diretamente na parte da "expressão" (ex: `numero * 2`).
* **Performance:** Além de reduzir o número de linhas, a List Comprehension é otimizada internamente pelo Python, sendo mais rápida que o método `.append()` dentro de um `for` tradicional.

---

### 🛠️ Anatomia da List Comprehension:



Diferente de um loop `for` comum que "pede" para adicionar itens, a List Comprehension "define" o que a lista deve conter de forma declarativa.

| Método | Código | Legibilidade |
| :--- | :--- | :--- |
| **For Loop** | 3-4 linhas | Explícito, mas longo |
| **List Comp** | 1 linha | Conciso e direto |

---

### 💡 Insight:
A regra de ouro da List Comprehension é: **não complique demais**. Se a sua expressão ficar muito longa ou difícil de ler, é melhor usar um loop `for` tradicional. O código deve ser escrito para que outros humanos (e você no futuro) consigam entender rapidamente.