# Aula 39 - Iterando Strings com `while` 📋

Nesta aula aprendi o conceito de iteração, que consiste em percorrer cada elemento de uma sequência (neste caso, uma string) um por um, utilizando um laço de repetição e seus índices.
In this class, I learned the concept of iteration, which consists of traversing each element of a sequence (in this case, a string) one by one, using a loop and its indices.

### :clipboard: O que aprendi / What I learned:

* **Strings como Iteráveis:** Entendi que strings são coleções de caracteres indexados que podem ser percorridos.
* **Acesso por Índice:** Como utilizar a variável de controle do `while` para acessar dinamicamente cada posição da string: `nome[index]`.
* **Construção de Novas Strings:** A técnica de acumular valores em uma variável vazia (`novo_nome += ...`) para transformar um dado original durante a iteração.
* **Atenção aos Limites:** A importância de usar `while i < len(string)` para evitar o erro `IndexError`, já que os índices param em `tamanho - 1`.

---

### 🛠️ Visualização da Iteração / Iteration Visualization:



| Passo (i) | Caractere | Resultado Acumulado (`novo_nome`) |
| :---: | :---: | :--- |
| 0 | L | `*L` |
| 1 | u | `*L*u` |
| 2 | i | `*L*u*i` |
| ... | ... | ... |

---

### 💡 Insight:
Iterar uma string com `while` nos dá um controle granular muito alto. Podemos decidir pular letras, alterar caracteres específicos ou até inverter a lógica de construção. É a base para algoritmos de criptografia simples, busca de padrões e limpeza de dados (Data Cleaning).