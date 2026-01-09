# Aula 34 - Introdução ao Laço de Repetição `while` 📋

Nesta aula aprendi a estrutura básica de repetição `while`. Ela permite que um bloco de código seja executado repetidamente enquanto uma determinada condição for verdadeira.
In this class, I learned the basic `while` loop structure. It allows a block of code to be executed repeatedly as long as a certain condition is true.

### :clipboard: O que aprendi / What I learned:

* **Controle de Fluxo:** O `while` verifica a condição no início de cada iteração.
* **Loop Infinito:** Entendi o risco de criar laços que nunca terminam e como evitá-los garantindo que a condição eventualmente se torne falsa.
* **Comando `break`:** Uma ferramenta poderosa para interromper o laço imediatamente, ignorando a condição do topo.
* **Interatividade:** Como usar o `while` para manter um programa rodando até que o usuário decida sair.

---

### 🛠️ Mecânica do While / While Mechanics:



| Comando | Função |
| :--- | :--- |
| `while <condicao>:` | Inicia o laço se a condição for True. |
| `break` | "Quebra" o laço e pula para a primeira linha após o bloco while. |
| `continue` | (Veremos adiante) Pula para a próxima iteração. |

---

### 💡 Insight:
O `while` é ideal quando não sabemos exatamente quantas vezes o código precisará se repetir (por exemplo, esperar o usuário digitar a senha correta). Diferente do `for`, que geralmente usamos para sequências finitas, o `while` foca na persistência de uma condição.