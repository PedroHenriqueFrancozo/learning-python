# Aula 16 - Controle de Fluxo Condicional 📋

Nesta aula aprendi a utilizar as estruturas `if`, `elif` e `else` para criar desvios lógicos no programa, permitindo que diferentes blocos de código sejam executados dependendo da condição.
In this class, I learned how to use `if`, `elif`, and `else` structures to create logical branches in the program, allowing different blocks of code to run depending on the condition.

### :clipboard: O que aprendi / What I learned:

* **`if` (Se):** A condição principal. Se for verdadeira, o bloco de código logo abaixo é executado.
* **`elif` (Se não se):** Utilizado para testar outras condições caso a primeira seja falsa. Podem existir múltiplos `elif`.
* **`else` (Se não):** O bloco executado caso nenhuma das condições anteriores seja atendida.
* **Identação:** A importância dos espaços (margem) para definir o que pertence a cada bloco lógico.

---

### 🛠️ Estrutura Lógica / Logic Structure:

| Comando | Descrição | Execução |
| :--- | :--- | :--- |
| **if** | Condição 1 | Executa se Condição 1 for `True` |
| **elif** | Condição 2 | Executa se Condição 1 for `False` e 2 for `True` |
| **else** | Padrão | Executa se todas as anteriores forem `False` |



---

### 💡 Insight:
O comando `print('FORA DOS BLOCOS')` demonstra que o fluxo do programa volta a ser linear após sair da estrutura condicional. Independentemente de qual caminho (entrar ou sair) o usuário escolher, o código que não estiver identado será executado normalmente após o fim do bloco de condições.