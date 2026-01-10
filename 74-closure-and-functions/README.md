# Aula 74 - Closure em Python 🔒

Nesta aula aprendi o conceito de **Closure** (Fechamento). Ocorre quando uma função interna "lembra" das variáveis de seu escopo externo, mesmo após a função externa ter sido finalizada.
In this class, I learned the concept of **Closure**. It occurs when an inner function "remembers" variables from its outer scope, even after the outer function has finished execution.

### :clipboard: O que aprendi / What I learned:

* **Funções que retornam funções:** Em vez de retornar um valor (str, int), a função externa retorna a própria definição de uma função interna.
* **Escopo Léxico:** A função interna `saudar` mantém acesso à variável `saudacao` que estava presente no momento da sua criação.
* **Customização de Comportamento:** Closures permitem criar funções altamente especializadas a partir de uma base comum (como criar saudações diferentes usando o mesmo "molde").

---

### 🛠️ Entendendo o Closure / Understanding Closure:



| Etapa | Ação |
| :--- | :--- |
| **Criação** | `falar_bom_dia = criar_saudacao('Bom dia')` - O valor 'Bom dia' é guardado. |
| **Execução** | `falar_bom_dia('Luiz')` - A função usa o valor guardado para completar a ação. |

---

### 💡 Insight:
O Closure é extremamente útil para evitar a repetição de código. Se você tem uma lógica complexa que muda apenas um detalhe (como o multiplicador de um número ou o prefixo de um texto), você usa um Closure em vez de criar várias funções quase idênticas ou usar variáveis globais.