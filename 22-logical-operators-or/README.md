# Aula 22 - Operador Lógico `or` e Valores Padrão 📋

Nesta aula aprendi o funcionamento do operador lógico `or`. Ao contrário do `and`, o `or` é mais "flexível": basta que **uma** das condições seja verdadeira para que toda a expressão seja considerada verdadeira.
In this class, I learned how the `or` logical operator works. Unlike `and`, the `or` operator is more "flexible": only **one** condition needs to be true for the entire expression to be true.

### :clipboard: O que aprendi / What I learned:

* **Lógica do `or`:** A expressão retorna o primeiro valor verdadeiro (Truthy) que encontrar.
* **Flexibilidade na Entrada:** Como usar o `or` para aceitar múltiplas variações de um comando (ex: 'E' ou 'e').
* **Curto-Circuito com `or`:** O Python interrompe a leitura assim que encontra um valor verdadeiro.
* **Valores Padrão:** Uma técnica poderosa para garantir que uma variável não fique vazia (ex: `input() or 'Valor Padrão'`).

---

### 🛠️ Tabela Verdade (or) / Truth Table (or):

| Condição A | Condição B | Resultado |
| :--- | :--- | :--- |
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |



[Image of logic gate or truth table]


---

### 💡 Insight:
O `or` é excelente para simplificar o código. No exemplo `senha = input('Senha: ') or 'Sem senha'`, se o usuário apenas apertar Enter (gerando uma string vazia `''`, que é **Falsy**), o Python pula para o próximo valor e atribui `'Sem senha'` à variável. Isso substitui 4 linhas de `if/else` por apenas uma!