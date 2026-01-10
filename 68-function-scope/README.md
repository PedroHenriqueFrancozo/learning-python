# Aula 68 - Escopo de Funções 📋

Nesta aula aprendi como o Python gerencia a visibilidade das variáveis. O conceito de escopo define onde uma variável nasce, vive e onde ela pode ser acessada.
In this class, I learned how Python manages variable visibility. The concept of scope defines where a variable is born, lives, and where it can be accessed.

### :clipboard: O que aprendi / What I learned:

* **Escopo Global:** Variáveis definidas fora de qualquer função. São acessíveis em todo o arquivo. / Variables defined outside any function. Accessible throughout the file.
* **Escopo Local:** Variáveis definidas dentro de uma função. Elas só existem enquanto a função está sendo executada. / Variables defined inside a function. They only exist while the function is running.
* **Palavra-chave `global`:** Permite que uma função altere uma variável que está no escopo global. / Allows a function to modify a variable in the global scope.
* **Hierarquia:** Funções internas podem acessar variáveis de funções externas (escopo de fechamento), mas o inverso não é verdadeiro.

---

### 🛠️ Visualização de Escopo / Scope Visualization:



| Escopo | Acessibilidade | Exemplo |
| :--- | :--- | :--- |
| **Global** | Todo o script. | `x = 1` (fora de tudo) |
| **Local** | Apenas dentro da função. | `y = 2` (dentro da def) |

---

### 💡 Insight:
Embora o comando `global` seja útil, em projetos grandes evitamos usá-lo com frequência. O ideal é que as funções sejam "puras": elas recebem dados por argumentos e devolvem dados pelo `return`, sem mexer em variáveis do lado de fora. Isso evita erros difíceis de encontrar (efeitos colaterais).