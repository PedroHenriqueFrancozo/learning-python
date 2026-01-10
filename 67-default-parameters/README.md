# Aula 67 - Valores Padrão para Parâmetros 📋

Nesta aula aprendi como tornar funções mais flexíveis definindo valores padrão para os parâmetros. Isso permite que a função seja chamada com diferentes quantidades de argumentos.
In this class, I learned how to make functions more flexible by setting default values for parameters. This allows the function to be called with different amounts of arguments.

### :clipboard: O que aprendi / What I learned:

* **Valores Padrão (Default Values):** São definidos no momento da criação da função (ex: `z=None`).
* **Tratamento com `None`:** Aprendi que usar `None` como valor padrão é uma excelente prática para identificar se um argumento foi ou não enviado pelo usuário.
* **Ordem dos Parâmetros:** Parâmetros com valores padrão devem sempre vir **depois** dos parâmetros sem valores padrão.
* **Refatoração (Refactoring):** O processo de editar o código para melhorar sua estrutura ou funcionalidade sem alterar seu comportamento final esperado.

---

### 🛠️ Regra de Posicionamento / Positioning Rule:



| Tipo | Exemplo | Obrigatoriedade |
| :--- | :--- | :--- |
| **Parâmetro Comum** | `x, y` | Obrigatório enviar valor. |
| **Parâmetro com Default** | `z=None` | Opcional (assume o padrão se omitido). |

---

### 💡 Insight:
Por que usar `z=None` em vez de `z=0`? Se você definir `z=0` e o usuário enviar `0`, você não saberá se ele realmente digitou `0` ou se o Python está usando o valor padrão. Com `None`, você consegue distinguir se o dado foi enviado ou não, tornando sua lógica muito mais precisa!