# Aula 72 - Exercícios Práticos com Funções 🧠

Nesta aula coloquei em prática os conceitos de `*args`, acumuladores e lógica condicional dentro de funções.
In this class, I practiced the concepts of `*args`, accumulators, and conditional logic within functions.

### :clipboard: Explicação dos Exercícios / Exercises Explanation:

#### 1. Multiplicador (`*args`):
* **O Desafio:** Criar uma função que aceite qualquer quantidade de números e retorne o produto deles.
* **Como foi feito:** * Utilizamos `*args` para empacotar os números em uma tupla.
    * Inicializamos a variável `total` com **1** (elemento neutro da multiplicação).
    * Usamos um laço `for` para multiplicar cada número pelo total acumulado.

#### 2. Par ou Ímpar:
* **O Desafio:** Criar uma função que identifique se um número é par ou ímpar.
* **Como foi feito:**
    * Utilizamos o operador de módulo `%`. 
    * `number % 2 == 0` verifica se o resto da divisão por 2 é zero.
    * Retornamos uma string formatada com o resultado.

---

### 🛠️ Conceitos Chave / Key Concepts:



| Operação | Lógica | Resultado esperado |
| :--- | :--- | :--- |
| **Multiplicação** | `total *= n` | Acúmulo de produto. |
| **Módulo (`%`)** | `n % 2` | Resto 0 (Par) ou Resto 1 (Ímpar). |

---

### 💡 Insight:
No exercício de par ou ímpar, você criou uma variável booleana `multiplo = number % 2 == 0`. Isso é excelente para a legibilidade do código! Em programação, chamamos isso de **"Flag"** ou variável de estado, que torna o `if` muito mais fácil de ler para outros desenvolvedores.