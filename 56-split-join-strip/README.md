# Aula 56 - Manipulação de Strings: `split`, `join` e `strip` 📋

Nesta aula aprendi métodos fundamentais para processar textos. Essas ferramentas são a base para trabalhar com arquivos CSV, entradas de usuários e formatação de logs.
In this class, I learned fundamental methods for processing text. These tools are the foundation for working with CSV files, user inputs, and log formatting.

### :clipboard: O que aprendi / What I learned:

* **Método `split()`:** Divide uma string em várias partes com base em um delimitador (espaço é o padrão) e retorna uma lista.
* **Método `strip()`:** Remove espaços em branco (ou caracteres específicos) das extremidades de uma string. Útil para "limpar" dados vindos de inputs sujos.
    * Variações: `lstrip()` (esquerda) e `rstrip()` (direita).
* **Método `join()`:** O inverso do split. Ele pega uma lista (ou qualquer iterável) e une seus elementos em uma única string, usando a string que chama o método como separador.
* **Imutabilidade:** Lembrei que strings são imutáveis; por isso, métodos como `strip()` não alteram a string original, mas retornam uma nova, que precisamos armazenar em uma lista ou variável.

---

### 🛠️ Visualização dos Métodos:



| Método | Entrada | Ação | Saída |
| :--- | :--- | :--- | :--- |
| `split(',')` | `'A,B,C'` | Divide pela vírgula | `['A', 'B', 'C']` |
| `strip()` | `'  A  '` | Remove espaços laterais | `'A'` |
| `'-'.join()` | `['A', 'B']` | Une com hífen | `'A-B'` |

---

### 💡 Insight:
O `join` é muito mais eficiente do que concatenar strings dentro de um laço `for` usando o operador `+`. Quando você usa `+` repetidamente, o Python cria uma nova string na memória a cada iteração. O `.join()` calcula o tamanho final necessário e cria a string de uma só vez, economizando processamento.