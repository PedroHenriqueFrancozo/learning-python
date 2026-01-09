# Aula 30 - Constantes e Complexidade de Código 📋

Nesta aula aprendi como escrever um código mais "limpo" (Clean Code). O foco foi substituir condições complexas dentro do `if` por variáveis que explicam a lógica e utilizar constantes para valores que não devem mudar.
In this class, I learned how to write cleaner code. The focus was on replacing complex conditions within `if` statements with variables that explain the logic and using constants for values that should not change.

### :clipboard: O que aprendi / What I learned:

* **Constantes:** Em Python, usamos nomes em **MAIÚSCULO** para indicar que um valor é uma constante e não deve ser alterado durante a execução.
* **Complexidade Cognitiva:** Quanto mais condições (`and`, `or`, `not`) em um único `if`, mais difícil é para um humano entender o código.
* **Refatoração de Lógica:** Criar variáveis booleanas com nomes descritivos (ex: `car_fined_at_radar_1`) torna o código "autoexplicativo".
* **Manutenibilidade:** Se a regra do radar mudar, alteramos apenas a variável lógica, e não todos os blocos `if` do sistema.

---

### 🛠️ Clean Code: Antes vs. Depois



| Conceito | Prática Ruim (Bad) | Prática Boa (Good) |
| :--- | :--- | :--- |
| **Valores Fixos** | Usar números "mágicos" (60, 100) no meio do código. | Usar `RADAR_1 = 60`. |
| **Condicionais** | `if v > 60 and l >= 99 and l <= 101:` | `if car_fined_at_radar_1:` |

---

### 💡 Insight:
O computador não se importa se o seu código é difícil de ler, mas o seu "eu" do futuro e seus colegas de trabalho sim. Escrever `if car_fined_at_radar_1:` é quase como ler uma frase em inglês, o que elimina a necessidade de comentários explicando o que aquela linha faz.