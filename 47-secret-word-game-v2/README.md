# Aula 47 - Exercício: Jogo da Palavra Secreta (V2) 📋

Nesta aula aperfeiçoei o jogo da palavra secreta utilizando uma lógica de acumulação de strings e introduzi a interação com o sistema operacional para limpar o console.
In this class, I improved the secret word game using string accumulation logic and introduced interaction with the operating system to clear the console.

### :clipboard: O que aprendi / What I learned:

* **Acumulação de Strings:** Em vez de listas, usamos uma string `letras_acertadas` para guardar o progresso do usuário.
* **Reconstrução de Strings:** A cada rodada, o programa reconstrói a `palavra_formada` percorrendo a palavra original e decidindo se mostra a letra ou um asterisco.
* **Módulo `os`:** Aprendi a usar `os.system('clear')` para limpar o lixo visual do terminal, tornando a experiência do usuário muito melhor.
* **Loop Infinito Controlado:** Uso do `while True` com uma condição de saída (`break`) baseada na vitória do jogador.

---

### 🛠️ Fluxo de Renderização / Rendering Flow:



| Variável | Papel no Jogo |
| :--- | :--- |
| `palavra_secreta` | O gabarito imutável. |
| `letras_acertadas` | Histórico de palpites corretos do usuário. |
| `palavra_formada` | O que é exibido na tela no momento (dinâmico). |

---

### 💡 Insight:
Note a diferença fundamental: na versão anterior (Aula 46), editávamos uma lista. Aqui, nós **recriamos** a string de exibição do zero a cada tentativa. Em Python, como strings são imutáveis, essa técnica de "reconstrução" dentro de um loop é muito comum para gerar saídas dinâmicas.