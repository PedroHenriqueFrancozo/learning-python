# Aula 71 - Argumentos Variáveis (`*args`) 📋

Nesta aula aprendi a usar o operador asterisco (`*`) para permitir que uma função receba uma quantidade ilimitada de argumentos não nomeados.
In this class, I learned how to use the asterisk operator (`*`) to allow a function to receive an unlimited number of non-named arguments.

### :clipboard: O que aprendi / What I learned:

* **Empacotamento com `*args`:** Quando definimos `*args` no parâmetro, o Python captura todos os argumentos posicionais e coloca-os dentro de uma **tupla**.
* **Flexibilidade:** A função torna-se capaz de processar 0, 1, 10 ou 1000 argumentos sem precisar mudar a sua definição.
* **Desempacotamento na Chamada:** Se já tenho uma lista ou tupla e quero passar os seus valores para a função, uso o `*` na chamada (ex: `soma(*numeros)`).
* **Convenção:** O nome `args` é uma convenção da comunidade Python, mas o que importa para o funcionamento é o símbolo asterisco (`*`).

---

### 🛠️ Diferença Visual / Visual Difference:

[Image showing arguments being packed into a tuple inside the function]

| Contexto | Acção | Exemplo |
| :--- | :--- | :--- |
| **Na Definição** | Empacota argumentos numa tupla. | `def func(*args):` |
| **Na Chamada** | Desempacota um iterável em argumentos. | `func(*lista)` |

---

### 💡 Insight:
O `*args` é o que permite que a função `print()` aceite vários valores separados por vírgula. Ao dominar isto, consegues criar ferramentas muito mais genéricas e potentes. Lembra-te apenas que os `args` são sempre uma **tupla**, o que significa que os valores são imutáveis dentro daquela coleção.