# Aula 70 - Retorno de Valores (Aprofundamento) 📋

Nesta aula, reforcei como capturar os resultados de uma função em variáveis e como o `return` funciona como um interruptor de execução.
In this class, I reinforced how to capture function results into variables and how `return` acts as an execution switch.

### :clipboard: O que aprendi / What I learned:

* **Captura de Dados:** Funções que retornam valores podem ter seus resultados armazenados em variáveis para cálculos futuros. / Functions that return values can have their results stored in variables for future calculations.
* **Retorno Condicional:** Uma função pode ter múltiplos caminhos de saída, retornando tipos de dados diferentes dependendo da lógica. / A function can have multiple exit paths, returning different data types depending on the logic.
* **Interrupção:** No momento em que o Python encontra um `return`, ele sai da função e ignora qualquer código que venha abaixo dele. / As soon as Python encounters a `return`, it exits the function and ignores any code below it.

---

### 🛠️ Comportamento do Return / Return Behavior:



| Código | O que acontece | Resultado |
| :--- | :--- | :--- |
| `soma(2, 2)` | Ignora o `if`, executa o `x + y`. | `4` |
| `soma(11, 5)` | Entra no `if`, retorna a lista e para. | `[10, 20]` |

---

### 💡 Insight:
O fato de uma função poder retornar tipos diferentes (como `int` e `list`) mostra a flexibilidade do Python (Tipagem Dinâmica). No entanto, em projetos profissionais, tentamos manter o retorno consistente (sempre o mesmo tipo) para evitar erros inesperados em quem for usar a função depois.