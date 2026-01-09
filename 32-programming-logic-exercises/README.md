# Aula 32 - Exercícios de Lógica e Robustez 📋

Nesta aula, além de resolver os desafios propostos, foquei em tornar o código mais robusto utilizando tratamento de exceções (`try/except`) e validações de tipos de dados.
In this class, besides solving the proposed challenges, I focused on making the code more robust using exception handling (`try/except`) and data type validations.

### :clipboard: O que aprendi / What I learned:

* **Tratamento Específico de Erros:** Aprendi a capturar exceções específicas como `ValueError` (erro de conversão) e `IndexError` (erro de índice).
* **Módulo `datetime`:** Introdução ao uso da biblioteca nativa para manipulação de horas. O método `strptime` é essencial para validar se uma string realmente representa um horário válido.
* **Validação de Strings:** Uso do método `.isalpha()` para garantir que o usuário digite apenas letras, evitando erros de lógica em campos de nome.
* **Refatoração para Robustez:** Entendi que um bom programa não apenas funciona, mas também sabe dizer ao usuário exatamente onde ele errou na entrada de dados.

---

### 🛠️ Desafios Resolvidos / Solved Challenges:

1. **Par ou Ímpar:** Conversão de tipo com proteção contra entradas não inteiras.
2. **Saudação por Horário:** Dois métodos aplicados (Split manual vs. Biblioteca Datetime).
3. **Tamanho de Nome:** Classificação baseada no comprimento da string com validação de caracteres.

---

### 💡 Insight:
A diferença entre usar `.isdigit()` ou `.isalpha()` e usar `try/except` é que os métodos de string verificam o **conteúdo**, enquanto o `try/except` lida com o **comportamento** do código. No Exercício 2, o `datetime` foi superior porque ele já sabe que "25:60" é uma hora impossível, algo que um simples `int(input)` não perceberia sozinho.