# Aula 21 - Operador Lógico `and` e Curto-Circuito 📋

Nesta aula aprendi o funcionamento do operador lógico `and`. Ele é exigente: para que a expressão final seja verdadeira, **todas** as condições individuais precisam ser verdadeiras.
In this class, I learned how the `and` logical operator works. It requires all individual conditions to be true for the final expression to be true.

### :clipboard: O que aprendi / What I learned:

* **Lógica do `and`:** A expressão retorna `True` apenas se todos os elementos forem verdadeiros.
* **Valores Falsy:** Entendi que no Python, valores como `0`, `0.0`, `''` (string vazia) e `False` são avaliados como falso em contextos lógicos.
* **Tipo `None`:** Utilizado para representar a ausência de valor.
* **Avaliação de Curto-Circuito:** O Python é inteligente; ao encontrar o primeiro valor falso em uma sequência de `and`, ele para a verificação e retorna aquele valor imediatamente.

---

### 🛠️ Tabela Verdade (and) / Truth Table (and):

| Condição A | Condição B | Resultado |
| :--- | :--- | :--- |
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |



[Image of logic gate and truth table]


---

### 💡 Insight:
A avaliação de curto-circuito é poderosa para performance e segurança. Por exemplo, você pode verificar se uma variável não é `None` **antes** de tentar acessar uma propriedade dela na mesma linha: `if user is not None and user.is_active:`. Se o primeiro for falso, o Python nem tenta ler o segundo, evitando erros!