# Aula 37 - Controle de Fluxo: `break` e `continue` 📋

Nesta aula aprendi a manipular o comportamento interno dos laços de repetição. O foco foi entender a diferença crucial entre interromper um laço e apenas pular uma de suas voltas (iterações).
In this class, I learned how to manipulate the internal behavior of loops. The focus was on understanding the crucial difference between interrupting a loop and simply skipping one of its turns (iterations).

### :clipboard: O que aprendi / What I learned:

* **O Comando `continue`:** Quando o interpretador encontra o `continue`, ele ignora todo o código que vem abaixo dele (dentro do bloco `while`) e volta imediatamente para o início do laço para testar a condição novamente.
* **O Comando `break`:** Encerra o laço de forma definitiva, movendo a execução para a primeira linha fora do bloco de repetição.
* **Lógica de Pular Intervalos:** Como usar operadores lógicos (`and`) junto com o `continue` para filtrar quais dados devem ou não ser processados.
* **Ordem de Execução:** A importância de incrementar o contador **antes** do `continue`, para evitar loops infinitos onde a condição nunca muda.

---

### 🛠️ Break vs. Continue:



| Comando | Ação | Destino do Fluxo |
| :--- | :--- | :--- |
| **`continue`** | Pula a iteração atual. | Volta para o teste da condição do `while`. |
| **`break`** | Interrompe o laço. | Sai do bloco `while` completamente. |

---

### 💡 Insight:
O `continue` é excelente para "limpar" os dados que você está processando. Imagine que você está lendo uma lista de 1000 nomes; você pode usar o `continue` para ignorar nomes vazios ou inválidos e continuar processando o resto sem precisar de uma estrutura de `if/else` gigantesca e aninhada.