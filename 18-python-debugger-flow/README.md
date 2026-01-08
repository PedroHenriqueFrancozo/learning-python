# Aula 18 - O Debugger e o Fluxo de Execução 📋

Nesta aula aprendi a utilizar o **Debugger do VS Code** para visualizar o interpretador do Python trabalhando em tempo real. Entender o "passo a passo" é essencial para encontrar erros e entender lógicas complexas.
In this class, I learned how to use the **VS Code Debugger** to visualize the Python interpreter working in real-time. Understanding the "step-by-step" is essential for debugging and understanding complex logic.

### :clipboard: O que aprendi / What I learned:

* **Breakpoints (Pontos de Parada):** Como pausar o programa em uma linha específica para analisar o estado das variáveis.
* **Execução Linha a Linha:** O uso do comando *Step Over* para avançar no código e ver quais blocos são saltados pelo interpretador.
* **Leitura do Interpretador:** Como o Python ignora os blocos `if` ou `elif` quando a condição é `False`, pulando direto para a próxima verificação.
* **Call Stack e Variables:** Onde observar o valor atual de cada variável durante a execução do programa.

---

### 🛠️ Ferramentas de Depuração / Debugging Tools:

| Botão | Nome | Função |
| :--- | :--- | :--- |
| **F5** | Start Debugging | Inicia o modo de depuração. |
| **F10** | Step Over | Pula para a próxima linha de código. |
| **F11** | Step Into | Entra dentro de uma função ou método. |
| **Shift+F5** | Stop | Para a execução do programa imediatamente. |


---

### 💡 Insight:
O Debugger revelou algo crucial: quando o Python encontra uma condição verdadeira (como a `condicao3`), ele executa o bloco e **"pula"** todas as condições restantes do mesmo grupo (`condicao4` e `else`), indo direto para o próximo comando fora do bloco. Isso economiza processamento e define a lógica de exclusividade.