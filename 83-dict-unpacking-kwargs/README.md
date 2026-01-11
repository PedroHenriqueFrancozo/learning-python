# Aula 83 - Empacotamento e Desempacotamento de Dicionários (`**kwargs`) 📦

Nesta aula, aprendi a manipular dicionários de forma avançada, utilizando o operador `**` para espalhar dados e a sintaxe `**kwargs` para funções que aceitam argumentos nomeados ilimitados.

### :clipboard: O que aprendi:

* **Merge de Dicionários:** O operador `**` dentro de chaves `{}` permite "despejar" o conteúdo de um dicionário dentro de outro de forma simples e elegante.
* **`**kwargs` (Keyword Arguments):** Enquanto o `*args` empacota argumentos posicionais em uma tupla, o `**kwargs` empacota argumentos nomeados (ex: `nome='Luiz'`) em um dicionário dentro da função.
* **Desempacotamento em Chamadas:** Posso passar um dicionário inteiro para uma função como se estivesse digitando cada argumento nomeado manualmente usando `funcao(**dicionario)`.

---

### 🛠️ Diferença entre Argumentos:



| Termo | Tipo de Dado | Exemplo de Chamada |
| :--- | :--- | :--- |
| **`*args`** | Tupla | `func(1, 2, 3)` |
| **`**kwargs`** | Dicionário | `func(a=1, b=2)` |

---

### 💡 Insight:
O uso de `**kwargs` é essencial para o princípio **Open/Closed** da programação. Ele permite que você adicione novos parâmetros às suas funções no futuro sem quebrar o código de quem já as utiliza, além de facilitar o repasse de configurações para outras funções internas.