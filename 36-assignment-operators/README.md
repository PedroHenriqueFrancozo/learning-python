# Aula 36 - Operadores de Atribuição Composta 📋

Nesta aula aprendi a utilizar operadores de atribuição combinados com operadores aritméticos. Essa técnica permite realizar cálculos e atualizar o valor de uma variável de forma muito mais concisa e legível.
In this class, I learned how to use assignment operators combined with arithmetic operators. This technique allows performing calculations and updating a variable's value in a much more concise and readable way.

### :clipboard: O que aprendi / What I learned:

* **Sintaxe Abreviada:** Em vez de escrever `x = x + 10`, podemos simplesmente usar `x += 10`.
* **Versatilidade:** Esses operadores funcionam com todas as operações matemáticas básicas (Soma, Subtração, Multiplicação, Divisão, etc.).
* **Tipagem:** Notei que ao usar `/=`, o resultado da variável pode ser convertido automaticamente para `float`, mesmo que o valor inicial fosse `int`.
* **Legibilidade:** O código fica mais limpo, reduzindo a poluição visual em algoritmos que envolvem muitos cálculos sucessivos na mesma variável.

---

### 🛠️ Tabela de Referência / Reference Table:

| Operador | Equivalente a | Descrição |
| :---: | :--- | :--- |
| `+=` | `x = x + y` | Adição e Atribuição |
| `-=` | `x = x - y` | Subtração e Atribuição |
| `*=` | `x = x * y` | Multiplicação e Atribuição |
| `/=` | `x = x / y` | Divisão e Atribuição |
| `//=` | `x = x // y` | Divisão Inteira e Atribuição |
| `**=` | `x = x ** y` | Potenciação e Atribuição |
| `%=` | `x = x % y` | Resto e Atribuição |



---

### 💡 Insight:
Embora o Python não possua os operadores de incremento `++` ou decremento `--` (comuns em C++ ou Java), o uso de `+= 1` e `-= 1` cumpre exatamente a mesma função de forma padronizada dentro da linguagem.