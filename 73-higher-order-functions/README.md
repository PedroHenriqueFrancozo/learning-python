# Aula 73 - Higher Order Functions & First-Class Functions 🚀

Nesta aula aprendi que em Python as funções são tratadas como "Cidadãs de Primeira Classe" (First-Class Citizens). Isso significa que elas podem ser atribuídas a variáveis, passadas como argumentos e retornadas por outras funções.
In this class, I learned that in Python functions are treated as "First-Class Citizens". This means they can be assigned to variables, passed as arguments, and returned by other functions.

### :clipboard: O que aprendi / What I learned:

* **First-Class Functions:** O conceito de que funções são objetos comuns. Posso fazer `v = soma` e depois chamar `v(1, 2)`.
* **Higher Order Functions (HOF):** Funções que recebem outras funções como parâmetro ou que retornam uma função. No nosso exemplo, a função `executa` é uma HOF.
* **Flexibilidade:** Isso permite criar códigos muito mais dinâmicos, onde o comportamento de uma função pode ser alterado dependendo de qual função enviamos para ela.

---

### 🛠️ Diferença Técnica / Technical Difference:

| Termo | Significado |
| :--- | :--- |
| **First-Class Functions** | A linguagem permite tratar funções como dados (inteiros, strings). |
| **Higher Order Functions** | O ato prático de uma função receber ou retornar outra função. |

---

### 💡 Insight:
Essa técnica é a base para conceitos avançados como **Decoradores** e funções integradas do Python como `map`, `filter` e `sort`. Quando você passa uma função para outra, você está separando a **lógica da execução** (quem executa) da **lógica da ação** (o que é feito).