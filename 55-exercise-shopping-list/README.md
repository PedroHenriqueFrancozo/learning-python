# Aula 54 - Exercício: Lista de Compras 📋

Nesta aula desenvolvi um sistema completo de lista de compras. O objetivo foi aplicar conhecimentos de listas, laços de repetição e tratamento de exceções para criar um programa robusto que não fecha mesmo com entradas incorretas do usuário.
In this class, I developed a complete shopping list system. The goal was to apply knowledge of lists, loops, and exception handling to create a robust program that doesn't crash even with incorrect user inputs.

### :clipboard: O que aprendi / What I learned:

* **Gerenciamento de CRUD:** Aprendi a Inserir (`append`), Ler (`for/enumerate`) e Deletar (`pop` ou `del`) itens de uma coleção.
* **Tratamento de Erros (`try/except`):** Fundamental para lidar com o `IndexError` (tentar apagar algo que não existe) e `ValueError` (digitar letras onde se esperava um índice numérico).
* **Interface de Usuário Simplificada:** Uso de menus baseados em caracteres únicos (`i`, `a`, `l`) para agilizar a interação.
* **Limpeza de Tela:** Integração com o sistema operacional para manter a interface organizada a cada ação.

---

### 🛠️ Fluxo de Operações / Operations Flow:



| Opção | Ação | Método Principal | Possível Erro |
| :--- | :--- | :--- | :--- |
| **i** | Inserir | `.append()` | - |
| **a** | Apagar | `.pop()` ou `.remove()` | `IndexError` / `ValueError` |
| **l** | Listar | `enumerate()` | - |

---

### 💡 Insight:
Este é o seu primeiro **CRUD** (Create, Read, Update, Delete). Quase todo sistema de software no mundo — do Instagram ao sistema do banco — é baseado nessas quatro operações. Dominar como manipular uma lista na memória é o primeiro passo para aprender a manipular bancos de dados no futuro.