# Exercícios Extras - Lógica com Loops `FOR` 🔁

Este repositório contém uma série de exercícios práticos para dominar o laço `for` em Python, focando em aplicações do mundo real como finanças e sistemas de busca.

### :clipboard: O que pratiquei:

* **Simulação Financeira:** Uso do `range()` para calcular juros compostos mês a mês, atualizando variáveis acumuladoras.
* **Padrão Flag (Bandeira):** Uso de variáveis booleanas (`found = False`) para rastrear o estado de uma busca dentro de uma lista.
* **Otimização com `break`:** Aprendi a encerrar um loop imediatamente após encontrar o resultado desejado, economizando processamento.
* **Formatação de Saída:** Uso do argumento `end=' '` no `print()` para exibir dados horizontalmente.
* **Tratamento de Exceções:** Implementação de `try/except` para evitar que o programa quebre caso o usuário digite um texto em vez de um número.

---

### 🛠️ Conceitos Chave:



| Conceito | Descrição | Exemplo |
| :--- | :--- | :--- |
| **Acomulador** | Variável que guarda a soma total. | `balance += interest` |
| **Range** | Gera uma sequência de números. | `range(1, 6)` (1 a 5) |
| **Flag** | Booleano que indica se algo aconteceu. | `found = True` |
| **End Argument** | Altera o caractere final do print. | `print(val, end=' ')` |

---

### 💡 Insight de Programador:
No exercício da busca de convidados, o `break` é fundamental. Imagine uma lista com 1 milhão de nomes; se o nome que você procura é o terceiro da lista, sem o `break` o computador continuaria verificando os outros 999.997 nomes sem necessidade. **Sempre pense em eficiência!**