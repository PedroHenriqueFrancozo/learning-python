# Aula 44 - A Função `range()` 📋

Nesta aula aprendi a utilizar a função `range()`, que é utilizada para gerar sequências numéricas de forma performática. Ela é essencial quando precisamos que um laço `for` execute um número específico de vezes.
In this class, I learned how to use the `range()` function, which is used to generate numeric sequences performantly. It is essential when we need a `for` loop to execute a specific number of times.

### :clipboard: O que aprendi / What I learned:

* **Parâmetros do `range`:**
    * `start`: Onde a sequência começa (inclusive).
    * `stop`: Onde a sequência termina (**exclusive** - o número final não entra).
    * `step`: O intervalo entre os números (passo).
* **Eficiência de Memória:** O `range` não cria todos os números de uma vez (como uma lista faria). Ele gera cada número apenas quando o `for` solicita, o que economiza muita memória em sequências grandes.
* **Flexibilidade:** Posso usar passos negativos para criar sequências decrescentes, como `range(10, 0, -1)`.

---

### 🛠️ Estrutura do Range / Range Structure:



| Exemplo | Resultado | Explicação |
| :--- | :--- | :--- |
| `range(5)` | `0, 1, 2, 3, 4` | Apenas o stop (começa em 0). |
| `range(2, 6)` | `2, 3, 4, 5` | Start em 2, stop em 6. |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` | Start 0, stop 10, de 2 em 2. |

---

### 💡 Insight:
O `range()` é um "iterável". Ele é como uma fôrma: ele tem o molde do que você quer, mas o "bolo" (os números) só existe quando o `for` passa por ele. Se você tentar dar um `print(range(0, 100))`, verá apenas o objeto, não os números. Para ver os números sem o `for`, você precisaria convertê-lo em uma lista: `list(range(0, 100))`.