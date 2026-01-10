# Aula 77 - Exercício: Sistema de Perguntas e Respostas 🧠

Nesta aula, apliquei o conhecimento de dicionários e listas para criar um sistema de Quiz funcional. O foco foi acessar dados aninhados e validar a entrada do usuário.
In this class, I applied dictionary and list knowledge to create a functional Quiz system. The focus was on accessing nested data and validating user input.

### :clipboard: O que aprendi / What I learned:

* **Estrutura de Dados Aninhada:** Como iterar sobre uma lista que contém dicionários, e como acessar listas dentro desses dicionários.
* **Lógica de Validação:** Uso do `.isdigit()` para garantir que o programa não quebre caso o usuário digite letras em vez de números.
* **Controle de Fluxo:** Implementação de contadores para rastrear o progresso do usuário (placar).
* **Indexação Dinâmica:** Uso do `enumerate()` para gerar opções numeradas e relacioná-las aos índices da lista de opções.

---

### 🛠️ Fluxo de Dados / Data Flow:



| Etapa | Ferramenta Usada |
| :--- | :--- |
| **Exibição** | `for` loop + `enumerate()` |
| **Entrada** | `input()` + `isdigit()` |
| **Verificação** | Índices de Lista + Comparação de Strings |
| **Resultado** | Contador acumulativo (`qtd_acertos`) |

---

### 💡 Insight:
Este exercício demonstra como os dicionários são ideais para representar "Objetos" do mundo real. Cada dicionário na lista `perguntas` age como um registro de banco de dados, mantendo os dados relacionados (pergunta, opções e resposta) agrupados em uma única unidade.