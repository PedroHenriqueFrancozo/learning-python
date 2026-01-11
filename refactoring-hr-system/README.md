# Exercício: Simulador de RH (Salário Líquido) 💰

Este exercício foca na **Refatoração** de um sistema de folha de pagamento. O objetivo foi transformar um código funcional em um código organizado, modular e fácil de manter.

### :clipboard: O que foi refatorado:

* **Separação de Responsabilidades:** Cada função agora faz apenas uma coisa (calcula bruto, aplica imposto ou aplica bônus).
* **Remoção de Prints Intermediários:** As funções de cálculo agora apenas retornam valores. A exibição foi centralizada em uma função de relatório.
* **Lógica de Bônus:** Ajustei para `hours > 160` (conforme o enunciado "mais de 160 horas").
* **Uso de Constantes:** Taxas e valores de bônus foram tratados como configurações fixas, facilitando mudanças futuras.

---

### 🛠️ Fluxo de Processamento de Dados:



| Etapa | Função | Input | Output |
| :--- | :--- | :--- | :--- |
| **1. Bruto** | `calculate_gross_salary` | Horas, Valor/H | Subtotal |
| **2. Imposto** | `apply_tax_discount` | Subtotal, % | Valor pós-taxa |
| **3. Bônus** | `apply_bonus` | Horas, Valor | Salário Final |

---

### 💡 Insight de Refatoração:
Ao remover os `print()` de dentro das funções de cálculo, tornamos essas funções "puras". Isso significa que elas podem ser reaproveitadas em outros lugares (como um site ou aplicativo móvel) sem poluir a tela com mensagens de texto desnecessárias. O cálculo e a exibição devem ser sempre independentes.