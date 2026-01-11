# Aula 81 - Funções Lambda (Anônimas) ƛ

Nesta aula, aprendi a utilizar funções Lambda para simplificar o código. Elas são funções sem nome, definidas em uma única linha, ideais para tarefas rápidas onde não queremos criar uma função completa com `def`.

### :clipboard: O que aprendi:

* **Sintaxe:** A estrutura básica é `lambda parametro: expressao`. O resultado da expressão é retornado automaticamente.
* **Uso com `sorted()`:** A função `sorted` não sabe como comparar dicionários sozinha. Usamos a lambda para dizer: "Ei, use o valor da chave 'nome' para decidir a ordem".
* **Praticidade:** Evita a criação de funções auxiliares que seriam usadas apenas uma vez no código.

---

### 🛠️ Estrutura de uma Lambda:



Ao contrário de uma função normal, a lambda:
1. Não possui o comando `return` explícito (ela retorna o que estiver na expressão).
2. Não possui nome.
3. É limitada a apenas **uma linha**.

| Característica | Função Normal (`def`) | Função Lambda |
| :--- | :--- | :--- |
| **Nome** | Obrigatório | Anônima |
| **Linhas** | Múltiplas | Apenas uma |
| **Complexidade** | Alta (lógicas complexas) | Baixa (lógicas simples) |

---

### 💡 Insight:
Embora úteis, as lambdas devem ser usadas com moderação. Se a lógica começar a ficar difícil de ler (muitos parênteses ou condições), é melhor voltar para uma função `def` para manter o código limpo e legível para outros desenvolvedores.