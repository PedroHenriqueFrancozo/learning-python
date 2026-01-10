# Aula 66 - Argumentos Nomeados e Não Nomeados 📋

Nesta aula aprendi como o Python lida com a passagem de valores para as funções. A flexibilidade de nomear argumentos permite que o código seja mais claro e menos dependente da ordem dos fatores.
In this class, I learned how Python handles passing values to functions. The flexibility of naming arguments allows the code to be clearer and less dependent on the order of factors.

### :clipboard: O que aprendi / What I learned:

* **Argumentos Posicionais (Positional Arguments):** O Python identifica o valor pela sua posição na chamada da função. / Python identifies the value by its position in the function call.
* **Argumentos Nomeados (Keyword Arguments):** Utilizamos o nome do parâmetro seguido de `=` para garantir que o valor vá para o lugar certo. / We use the parameter name followed by `=` to ensure the value goes to the right place.
* **Regra de Ouro (Golden Rule):** Uma vez que você utiliza um argumento nomeado, todos os seguintes devem ser nomeados. / Once you use a named argument, all subsequent ones must also be named.

---

### 🛠️ Visualização / Visualization:



| Tipo / Type | Exemplo / Example | Descrição / Description |
| :--- | :--- | :--- |
| **Posicional** | `soma(1, 2, 3)` | Segue a ordem: x=1, y=2, z=3. / Follows the order. |
| **Nomeado** | `soma(x=1, y=2, z=3)` | O nome define o destino. / The name defines the destination. |

---

### 💡 Insight:
O uso de `f'{x=}'` é uma das formas mais eficientes de entender o que está acontecendo dentro das suas funções (debugging). Ele elimina a necessidade de escrever textos manuais para identificar qual variável está sendo impressa.
Using `f'{x=}'` is one of the most efficient ways to understand what is happening inside your functions (debugging). It removes the need to write manual labels to identify which variable is being printed.