# Aula 29 - Introdução ao `try/except` 📋

Nesta aula aprendi a tratar exceções no Python. O bloco `try/except` é utilizado para capturar erros que interromperiam a execução do programa (runtime errors), permitindo que o desenvolvedor decida como o sistema deve reagir à falha.
In this class, I learned how to handle exceptions in Python. The `try/except` block is used to catch runtime errors, allowing the developer to decide how the system should respond to a failure.

### :clipboard: O que aprendi / What I learned:

* **Bloco `try`:** O código que "tentamos" executar. Se algo der errado dentro dele, o Python pula imediatamente para o erro.
* **Bloco `except`:** Onde definimos o "plano B" caso ocorra uma falha no `try`.
* **Fail Fast vs. Robustness:** Entendi que é melhor tratar o erro do que usar verificações complexas como `.isdigit()` que podem falhar com números negativos ou decimais.
* **Experiência do Usuário:** Como evitar que o usuário veja mensagens de erro técnicas e confusas, substituindo-as por mensagens amigáveis.

---

### 🛠️ Fluxo de Execução / Execution Flow:



[Image of Python try except flow chart]


| Situação | Caminho Percorrido |
| :--- | :--- |
| **Entrada Válida** (`10`) | `try` completo ➔ Pula o `except` |
| **Entrada Inválida** (`abc`) | Inicia o `try` ➔ Erro na conversão ➔ Executa `except` |

---

### 💡 Insight:
No Python, existe uma filosofia chamada **EAFP** (*Easier to Ask for Forgiveness than Permission*), ou "É mais fácil pedir perdão do que permissão". Em vez de checar mil vezes se o dado é válido antes de usar, nós tentamos usá-lo dentro de um `try` e tratamos a exceção se ela vier. Isso torna o código mais limpo e rápido!