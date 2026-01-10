# Aula 46 - Exercício Prático: Jogo da Palavra Secreta 📋

Nesta aula apliquei os conceitos de laços de repetição (`while` e `for`) e listas para criar um jogo de adivinhação. O desafio foi gerenciar o estado da palavra conforme o usuário acertava as letras.
In this class, I applied the concepts of loops (`while` and `for`) and lists to create a guessing game. The challenge was managing the word state as the user correctly guessed letters.

### :clipboard: O que aprendi / What I learned:

* **Gerenciamento de Estado:** Usei uma lista de asteriscos (`['*'] * len`) que é atualizada dinamicamente.
* **Busca com Enumerate:** A função `enumerate` foi essencial para identificar a posição exata (índice) onde a letra correta deveria ser revelada.
* **Condição de Parada Dinâmica:** O `while '*' in discovered_letters` é uma forma elegante de manter o jogo rodando enquanto ainda houver partes ocultas.
* **Manipulação de Strings e Listas:** Uso do método `' '.join()` para transformar a lista de progresso em uma string visualmente agradável para o usuário.

---

### 🛠️ Lógica de Atualização / Update Logic:



| Estado Inicial | Input | Processamento | Estado Final |
| :--- | :---: | :--- | :--- |
| `['*', '*', '*']` | 'a' | Letra encontrada no índice 1 | `['*', 'a', '*']` |
| `['*', 'a', '*']` | 'z' | Letra não encontrada | `['*', 'a', '*']` |

---

### 💡 Insight:
Este exercício simula a lógica básica de muitos sistemas de busca e filtragem. A separação entre a **Palavra Secreta** (o dado original) e as **Letras Descobertas** (a visualização do usuário) é um conceito fundamental de arquitetura de software: nunca altere o dado original se você precisar dele para comparação posterior.