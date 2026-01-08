# Aula 15 - Coleta de Dados e Coerção 📋

Nesta aula aprendi a interagir com o usuário através da função `input()` e a importância de converter os tipos de dados para realizar operações.
In this class, I learned how to interact with the user through the `input()` function and the importance of converting data types to perform operations.

### :clipboard: O que aprendi / What I learned:

* **Função `input()`:** Como capturar dados digitados pelo usuário no terminal.
* **Tipagem Padrão:** O entendimento de que todo dado vindo de um input é, por padrão, uma **String**.
* **Coerção de Tipos (Typecasting):** Como transformar uma string em um inteiro (`int`) para possibilitar cálculos matemáticos.

---

### 🛠️ Exemplo de Fluxo / Process Example:

| Etapa | Código | Resultado Interno |
| :--- | :--- | :--- |
| **Entrada** | `input('...')` | `'10'` (Texto/String) |
| **Conversão** | `int('10')` | `10` (Número/Integer) |
| **Operação** | `10 + 10` | `20` (Resultado) |

---

### 💡 Insight:
Realizar a coerção de tipos logo após o `input` é uma boa prática para evitar erros inesperados. Se tentarmos somar as variáveis sem converter, o Python fará uma **concatenação** (ex: '10' + '10' vira '1010') em vez de uma soma aritmética.