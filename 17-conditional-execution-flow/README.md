# Aula 17 - Lógica de Fluxo e Condições Independentes 📋

Nesta aula aprofundei o conhecimento sobre como o Python processa blocos condicionais, focando na exclusividade do `elif` e na independência de múltiplos blocos `if`.
In this class, I deepened my knowledge of how Python processes conditional blocks, focusing on `elif` exclusivity and the independence of multiple `if` blocks.

### :clipboard: O que aprendi / What I learned:

* **Exclusividade do Bloco:** Em um bloco `if/elif/else`, o Python executa apenas o **primeiro** código cuja condição for verdadeira e ignora todo o resto do bloco, mesmo que as condições seguintes também sejam verdadeiras.
* **Blocos Independentes:** Quando iniciamos um novo `if` sem o `elif`, criamos uma nova árvore de decisão que será avaliada independentemente da anterior.
* **Escopo e Identação:** Reforcei como o Python utiliza o recuo para determinar quais linhas de código pertencem a qual decisão.

---

### 🛠️ Comportamento do Fluxo / Flow Behavior:

| Estrutura | Comportamento |
| :--- | :--- |
| **if / elif** | "Apenas um vence". O primeiro `True` para a execução do bloco. |
| **Múltiplos `if`** | Cada um é uma pergunta nova. Todos podem ser executados se forem `True`. |
| **Linhas sem recuo** | Sempre são executadas, pois estão fora da árvore de decisão. |


---

### 💡 Insight:
No código desta aula, embora as condições 1, 2, 3 e 4 sejam todas `True`, apenas o código da **condição 1** foi exibido. Isso prova que o `elif` só é verificado se o `if` (ou o `elif` anterior) for **falso**. Já o `if 10 == 10` foi executado porque ele inicia uma estrutura lógica totalmente nova.