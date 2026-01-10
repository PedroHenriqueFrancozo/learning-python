# Aula 55 - Imprecisão de Ponto Flutuante (IEEE 754) 📋

Nesta aula aprendi por que cálculos com números decimais podem apresentar resultados estranhos no computador e como resolver isso quando a precisão é crítica (como em sistemas financeiros).
In this class, I learned why decimal calculations can show strange results on computers and how to solve this when precision is critical (like in financial systems).

### :clipboard: O que aprendi / What I learned:

* **O Padrão IEEE 754:** Computadores representam números decimais em binário. Assim como não conseguimos escrever $1/3$ de forma exata em decimal ($0.333...$), o computador não consegue representar certas frações decimais perfeitamente em binário.
* **O Módulo `decimal`:** Fornece o tipo `Decimal` para cálculos aritméticos de precisão fixa ou flutuante.
* **Strings no Decimal:** Aprendi que devo passar o número como **string** (`'0.1'`) para o `Decimal`, pois se passar como float, o Python já entregará o número com a imprecisão binária.
* **Função `round()`:** Uma forma rápida de arredondar valores para exibição ou cálculos menos críticos.

---

### 🛠️ Comparação de Precisão:



| Método | Uso Recomendado | Resultado de $0.1 + 0.7$ |
| :--- | :--- | :--- |
| **`float`** | Cálculos científicos, jogos, performance. | `0.7999999999999999` |
| **`round()`** | Exibição visual simples. | `0.8` |
| **`Decimal`** | Dinheiro, contabilidade, cálculos críticos. | `0.8` (Exato) |

---

### 💡 Insight:
Em sistemas bancários, **nunca** se usa o tipo `float`. Um erro na 15ª casa decimal pode parecer pouco, mas em milhões de transações, isso se torna um prejuízo (ou lucro indevido) enorme. O `Decimal` é o seu melhor amigo para garantir que cada centavo seja contado corretamente.