# Aula 40 - Projeto: Calculadora com `while` 📋

Nesta aula apliquei os conhecimentos acumulados para criar uma calculadora robusta que trata erros de digitação e permite múltiplas operações sem fechar o programa.
In this class, I applied accumulated knowledge to create a robust calculator that handles typing errors and allows multiple operations without closing the program.

### :clipboard: O que aprendi / What I learned:

* **Validação de Dados:** O uso do `try/except` para impedir que o programa quebre se o usuário digitar letras no lugar de números.
* **Flags de Controle:** Uso da variável `valid_numbers` (None/True) para controlar o fluxo do programa.
* **Operadores de Associação (`in`):** Verificação eficiente se o operador digitado faz parte da lista permitida.
* **Métodos de String Encadeados:** Uso de `.lower().startswith('s')` para criar uma interface de saída mais amigável e tolerante a erros do usuário (aceita "Sim", "s", "sim").
* **Estrutura de Repetição Infinita:** O uso de `while True` para manter o software rodando até que o comando de saída explícito seja acionado.

---

### 🛠️ Fluxograma da Lógica / Logic Flow:



| Verificação | Ferramenta Utilizada | Motivo |
| :--- | :--- | :--- |
| Números | `try/except float()` | Evitar crash por entrada de texto. |
| Operador | `if operator not in '+-/*'` | Garantir que a operação é suportada. |
| Tamanho | `if len(operator) > 1` | Impedir operadores compostos ou inválidos. |
| Saída | `.startswith('s')` | Facilitar a resposta do usuário. |

---

### 💡 Insight:
Uma calculadora profissional não é apenas sobre matemática, é sobre **segurança de dados**. O código que realiza a conta (`+`, `-`, etc.) é pequeno comparado ao código necessário para garantir que os dados inseridos são válidos. Tratar exceções é 80% do trabalho de um desenvolvedor.