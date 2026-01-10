# Aula 42 - Algoritmo: Letra que apareceu mais vezes 📋

Nesta aula desenvolvi um algoritmo para analisar a frequência de caracteres em uma string. O objetivo foi identificar qual letra (excluindo espaços) ocorre com mais frequência dentro de um texto.
In this class, I developed an algorithm to analyze character frequency in a string. The goal was to identify which letter (excluding spaces) occurs most frequently within a text.

### :clipboard: O que aprendi / What I learned:

* **Método `.count()`:** Utilizado para contar a ocorrência de um determinado caractere ou sub-string dentro de uma string maior.
* **Lógica de Comparação:** Implementação de uma variável "campeã" (`max_frequency`) que é atualizada sempre que uma contagem maior é encontrada.
* **Filtragem de Dados:** Uso do `continue` para ignorar espaços vazios, garantindo que o resultado foque apenas em letras/caracteres visíveis.
* **Iteração Completa:** O laço percorre cada caractere, garantindo que nenhum dado seja ignorado na análise.

---

### 🛠️ Lógica do Algoritmo / Algorithm Logic:



| Variável | Função |
| :--- | :--- |
| `frase.count(letra)` | Conta quantas vezes a letra alvo aparece no texto todo. |
| `max_frequency` | Armazena o maior número de ocorrências encontrado até o momento. |
| `most_frequent_letter` | Armazena o caractere correspondente ao recorde de frequência. |

---

### 💡 Insight:
Embora funcional, este algoritmo tem uma complexidade maior porque o `.count()` percorre a string inteira para **cada** letra do `while`. Em frases gigantescas, isso pode ser lento. No futuro, aprenderemos ferramentas como `Dictionaries` ou a biblioteca `collections.Counter` que resolvem isso de forma muito mais performática!