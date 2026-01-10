# Aula 69 - Retorno de Valores (`return`) 📋

Nesta aula aprendi como extrair dados de dentro de uma função. O `return` é a palavra-chave que permite que o resultado de um processamento interno seja utilizado em outras partes do código.
In this class, I learned how to extract data from within a function. The `return` keyword allows the result of internal processing to be used in other parts of the code.

### :clipboard: O que aprendi / What I learned:

* **O papel do `return`:** Ele para a execução da função imediatamente e envia um valor para o chamador. / It stops function execution immediately and sends a value to the caller.
* **Função sem `return`:** Aprendi que, sem essa palavra, a função executa sua lógica mas devolve sempre `None`. / Without this keyword, the function executes its logic but always returns `None`.
* **Flexibilidade:** Uma função pode retornar qualquer tipo de dado (int, str, list, dict, ou até outra função). / A function can return any data type.
* **Múltiplos retornos:** Embora uma função só possa retornar uma vez, podemos ter vários `return` dentro de estruturas condicionais (`if/else`).

---

### 🛠️ Fluxo de Trabalho / Workflow:



| Ação | Descrição | Description |
| :--- | :--- | :--- |
| **Input** | Argumentos entram na função. | Arguments enter the function. |
| **Process** | A lógica é executada. | The logic is executed. |
| **Output** | O `return` envia o resultado para fora. | The `return` sends the result out. |

---

### 💡 Insight:
O `return` funciona como o ponto final de um parágrafo. Nada que for escrito dentro da função **depois** do `return` será executado. É uma forma eficiente de "sair mais cedo" de uma função (técnica de *Early Return*) caso uma condição específica seja atingida.