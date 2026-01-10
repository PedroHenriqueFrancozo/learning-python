# Aula 75 - Exercício: Fábrica de Multiplicadores 🏭

Neste exercício, apliquei o conceito de **Closure** para resolver um problema de repetição de código. Em vez de definir múltiplas funções manualmente, criei uma "fábrica" que gera funções sob medida.
In this exercise, I applied the **Closure** concept to solve a code repetition problem. Instead of defining multiple functions manually, I created a "factory" that generates tailored functions.

### :clipboard: Explicação do Desafio / Challenge Explanation:

* **O Problema:** Precisávamos de três comportamentos diferentes (dobrar, triplicar, quadruplicar).
* **A Solução Antiga (Comentada):** Criar `duplicate()`, `triple()` e `quadruple()` individualmente geraria redundância.
* **A Solução com Closure:**
    * A função `criar_multiplicador` recebe o fator de multiplicação.
    * Ela retorna a função `multiplicar` que já "nasce" sabendo por quanto deve multiplicar qualquer número que receber.

---

### 🛠️ Comparação de Estrutura / Structure Comparison:



| Abordagem | Repetição de Código | Flexibilidade |
| :--- | :--- | :--- |
| **Individual** | Alta (Redundante) | Baixa |
| **Closure (Fábrica)** | Mínima | Alta (Posso criar um `x100` facilmente) |

---

### 💡 Insight:
Este padrão é conhecido como **Factory Pattern** (Padrão Fábrica). Ele é extremamente útil quando você tem uma lógica base que se repete, mudando apenas uma configuração ou valor inicial. Isso torna seu código **DRY** (*Don't Repeat Yourself*).