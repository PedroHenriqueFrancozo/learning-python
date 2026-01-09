# Aula 27 - Fatiamento de Strings e Função `len` 📋

Nesta aula aprendi a técnica de fatiamento (*slicing*), que permite extrair partes específicas de uma string, e utilizei a função `len` para contar o número de caracteres em um texto.
In this class, I learned the slicing technique, which allows extracting specific parts of a string, and used the `len` function to count the number of characters in a text.

### :clipboard: O que aprendi / What I learned:

* **Sintaxe do Fatiamento:** O formato `[início:fim:passo]`.
* **Índice de Parada:** Entendi que o índice final (stop) **não é incluído** no resultado (é exclusivo).
* **O Passo (Step):** Como pular caracteres ou inverter a ordem da string usando um passo negativo (`-1`).
* **Função `len()`:** Uma função nativa do Python que retorna a quantidade total de itens em um iterável (neste caso, caracteres em uma string).

---

### 🛠️ Guia de Fatiamento / Slicing Guide:

| Comando | Resultado | Explicação |
| :--- | :--- | :--- |
| `str[0:3]` | Primeiros 3 chars | Começa no 0 e para antes do 3. |
| `str[4:]` | Do índice 4 ao fim | Omissão do fim significa "até o resto". |
| `str[::-1]` | String invertida | Inicia e termina nos extremos com passo negativo. |
| `len(str)` | Inteiro (ex: 9) | Retorna o tamanho total da string. |

[Image representing Python string slicing with start, stop, and step parameters]

---

### 💡 Insight:
O fatiamento `[::-1]` é um exemplo clássico da simplicidade do Python. Em linguagens como Java ou C, você precisaria de um laço `for` complexo para inverter uma string. No Python, o interpretador resolve isso internamente de forma otimizada com apenas alguns caracteres.