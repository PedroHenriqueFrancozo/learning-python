# Aula 35 - Contadores e Controle de Fluxo no `while` 📋

Nesta aula aprendi como utilizar variáveis de controle, conhecidas como contadores, para determinar exatamente quantas vezes um laço `while` deve ser executado.
In this class, I learned how to use control variables, known as counters, to determine exactly how many times a `while` loop should execute.

### :clipboard: O que aprendi / What I learned:

* **Variável de Controle:** A importância de inicializar uma variável (ex: `contador = 0`) antes de iniciar o laço.
* **Incremento:** O processo de somar um valor à variável de controle dentro do bloco (`contador = contador + 1`) para que a condição de parada seja atingida.
* **Lógica de Comparação:** Como os operadores relacionais (`<`, `<=`, `>`) definem o limite exato de repetições.
* **Prevenção de Loop Infinito:** Entendi que se esquecermos de incrementar o contador, a condição `True` nunca mudará, travando o programa.

---

### 🛠️ Estrutura do Contador:



| Parte do Código | Função |
| :--- | :--- |
| `contador = 0` | **Inicialização:** Define o ponto de partida. |
| `while contador < 10:` | **Condição:** Define o ponto de parada. |
| `contador = contador + 1` | **Atualização:** Garante que o laço avance. |

---

### 💡 Insight:
O contador é como o ponteiro de um relógio. Sem o movimento constante (incremento), o tempo (execução) fica parado no mesmo lugar. Em Python, também é comum ver o atalho `contador += 1` para realizar o incremento de forma mais concisa.