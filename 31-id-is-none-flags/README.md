# Aula 31 - Identidade, Flags e o tipo `None` 📋

Nesta aula aprendi como o Python identifica objetos na memória e como utilizar o valor `None` para criar "bandeiras" (flags) que ajudam a rastrear se um determinado bloco de código foi executado.
In this class, I learned how Python identifies objects in memory and how to use the `None` value to create flags that help track whether a specific block of code was executed.

### :clipboard: O que aprendi / What I learned:

* **Função `id()`:** Cada objeto no Python recebe um identificador único (o endereço de memória).
* **Operador `is` e `is not`:** Diferente do `==` (que compara valor), o `is` compara se os objetos são **exatamente o mesmo** na memória.
* **O tipo `None`:** Representa a ausência de valor. É ideal para inicializar variáveis que serão preenchidas condicionalmente.
* **Conceito de Flag:** Uma variável (bandeira) que "marca" se o fluxo do programa passou por um ponto específico.

---

### 🛠️ Identidade vs. Valor / Identity vs. Value:



| Comparação | O que verifica? | Exemplo |
| :--- | :--- | :--- |
| `==` | Se os **valores** são iguais. | `1.0 == 1` (True) |
| `is` | Se a **identidade (id)** é a mesma. | `1.0 is 1` (False) |
| `is None` | Se a variável não possui valor. | `var is None` |

---

### 💡 Insight:
Usar `if variavel is None:` é muito mais seguro do que usar `if not variavel:`. O `not` retornaria verdadeiro para o número `0`, para uma string vazia `''` ou para `False`. Já o `is None` garante que você está verificando estritamente se a variável não foi inicializada com um valor real.