# Aula 33 - Tipos Embutidos e Imutabilidade 📋

Nesta aula explorei a documentação oficial do Python e entendi o conceito de objetos imutáveis. Tipos como `str`, `int`, `float` e `bool` não podem ser alterados após serem criados na memória.
In this class, I explored the official Python documentation and understood the concept of immutable objects. Types like `str`, `int`, `float`, and `bool` cannot be changed after they are created in memory.

### :clipboard: O que aprendi / What I learned:

* **Imutabilidade:** Se eu precisar alterar uma string, o Python na verdade cria um novo endereço de memória com o novo valor, deixando a original intacta (ou descartando-a se não houver referências).
* **Métodos de String:** Conheci o método `.zfill(n)`, que preenche a string com zeros à esquerda até atingir o tamanho `n`.
* **Consulta à Documentação:** A importância de verificar a [documentação oficial](https://docs.python.org/pt-br/3/library/stdtypes.html) para entender o comportamento dos tipos padrão.

---

### 🛠️ Exemplo de Imutabilidade na Memória:



| Operação | Resultado na Memória |
| :--- | :--- |
| `nome = 'Luiz'` | Cria objeto `'Luiz'` no ID 101. |
| `nome = 'João'` | Cria novo objeto `'João'` no ID 102. O ID 101 é descartado. |

---

### 💡 Insight:
Saber que strings são imutáveis explica por que métodos como `.upper()` ou `.replace()` não alteram a variável original sozinha; você sempre precisa atribuir o resultado de volta à variável: `nome = nome.upper()`. Sem a atribuição, a transformação "se perde" no vácuo.