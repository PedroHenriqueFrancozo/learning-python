# Aula 14 - Método de Formatação `.format()` 📋

Nesta aula aprendi a usar o método `.format()`, uma alternativa poderosa às f-strings para formatar textos e gerenciar variáveis dentro de strings.
In this class, I learned how to use the `.format()` method, a powerful alternative to f-strings for text formatting and managing variables within strings.

### :clipboard: O que aprendi / What I learned:

* **Argumentos Nomeados:** Como atribuir nomes às variáveis dentro do método para facilitar a leitura e organização do código.
* **Reutilização de Dados:** A capacidade de repetir o mesmo valor na string referenciando o mesmo nome (ex: `{nome1}`) várias vezes.
* **Formatação de Decimais:** O uso de parâmetros como `:.2f` para controlar a precisão de números reais (floats).

---

### 🛠️ Exemplo de Formatação / Formatting Example:

| Código | Resultado Esperado | Explicação |
| :--- | :--- | :--- |
| `{n1}` | Valor da variável | Referência por nome (Named argument) |
| `{n1:.2f}` | `1.10` | Nome + 2 casas decimais (Precision) |
| `format(n1=a)` | Valor atribuído | Atribuição manual dentro do método |

---

### 💡 Insight:
O método `.format()` é extremamente útil quando você precisa separar a criação da "máscara" da string (o template) da inserção dos dados reais, permitindo que a mesma estrutura de texto seja alimentada por diferentes fontes de dados ao longo do programa.