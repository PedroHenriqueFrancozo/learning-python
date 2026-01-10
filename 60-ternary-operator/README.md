# Aula 60 - Operação Ternária 📋

Nesta aula aprendi a utilizar a operação ternária, uma ferramenta que permite simplificar expressões condicionais em uma única linha de código.
In this class, I learned how to use the ternary operator, a tool that allows simplifying conditional expressions into a single line of code.

### :clipboard: O que aprendi / What I learned:

* **Sintaxe do Ternário:** A estrutura segue a lógica: `resultado = valor_se_verdadeiro if condicao else valor_se_falso`.
* **Atribuição Condicional:** É ideal para definir o valor de uma variável dependendo de uma verificação rápida.
* **Legibilidade:** Embora reduza o número de linhas, aprendi que deve ser usada com moderação. Se a condição for muito longa, o `if/else` tradicional é preferível.
* **Ordem de Avaliação:** O Python primeiro avalia a `condicao`. Se for `True`, ele retorna o que está à esquerda; se for `False`, retorna o que está à direita.

---

### 🛠️ Estrutura Lógica / Logical Structure:



| Componente | Função | Exemplo |
| :--- | :--- | :--- |
| **Valor Inicial** | Retorno caso a condição seja verdadeira. | `'Aprovado'` |
| **`if` Condição** | O teste lógico a ser feito. | `if media >= 7` |
| **`else` Valor** | Retorno caso a condição seja falsa. | `else 'Reprovado'` |

---

### 💡 Insight:
A operação ternária é muito usada em "List Comprehensions" e em retornos de funções simples. No entanto, lembre-se do Zen of Python: **"Legibilidade conta"**. Se você precisar ler a linha três vezes para entender o que ela faz, é melhor usar quatro linhas com um `if/else` comum do que uma linha com um ternário complexo.