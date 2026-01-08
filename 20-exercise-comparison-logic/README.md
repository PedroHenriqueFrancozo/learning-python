# Aula 20 - Exercício Prático: Comparação de Valores 📋

Nesta aula, realizei um exercício prático para aplicar os conceitos de entrada de dados e lógica condicional, comparando dois valores digitados pelo usuário.
In this class, I completed a practical exercise to apply data input and conditional logic concepts by comparing two user-provided values.

### :clipboard: O que aprendi / What I learned:

* **Lógica de Comparação:** Como estruturar um desvio condicional para identificar qual valor é maior.
* **Refatoração de f-strings:** O uso de f-strings para exibir mensagens claras e dinâmicas no console.
* **Atalho de Debugging:** Aprendi que ao usar `{variavel=}` dentro de uma f-string, o Python exibe o nome da variável seguido do seu valor (ex: `first_value='10'`).

---

### 🛠️ Exemplo de Execução / Execution Example:

| Entrada 1 | Entrada 2 | Resultado Esperado |
| :--- | :--- | :--- |
| `10` | `5` | `primeiro_valor=10 é maior ou igual que segundo_valor=5` |
| `3` | `8` | `segundo_valor=8 é maior do que primeiro_valor=3` |

---

### 💡 Insight:
Embora o código funcione bem, é importante lembrar que os valores vindos do `input` são strings. Em uma comparação como `'10' > '2'`, o Python compara a ordem alfabética (lexicográfica). Para uma comparação numérica precisa em um sistema real, o ideal seria converter os valores para `int` ou `float` antes da comparação.