# Aula 23 - Operador Lógico `not` 📋

Nesta aula aprendi o funcionamento do operador `not`. Ele é usado para inverter o valor booleano de uma expressão: o que é verdadeiro vira falso, e o que é falso vira verdadeiro.
In this class, I learned how the `not` operator works. It is used to invert the boolean value of an expression: what is true becomes false, and what is false becomes true.

### :clipboard: O que aprendi / What I learned:

* **Inversão de Valores:** O `not` transforma `True` em `False` e vice-versa.
* **Verificação Negativa:** Como usar o `not` para testar se algo **não** aconteceu ou se um valor está vazio.
* **Simplificação de Lógica:** Em muitos casos, é mais fácil ler "se não houver erro" (`if not error`) do que comparar com valores específicos.

---

### 🛠️ Tabela da Inversão / Inversion Table:

| Expressão Original | Resultado com `not` |
| :--- | :--- |
| `True` | `False` |
| `False` | `True` |
| `bool('')` (Falsy) | `True` |
| `bool('abc')` (Truthy) | `False` |


[Image of logic gate not truth table]


---

### 💡 Insight:
O operador `not` é extremamente útil para verificar "vazios". Como strings vazias, o número 0 e listas vazias são considerados **Falsy**, usar `if not valor:` é a forma mais elegante em Python de dizer: "Se o usuário não digitou nada" ou "Se a lista está vazia".