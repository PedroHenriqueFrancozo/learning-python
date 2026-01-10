# Aula 65 - Introdução às Funções (`def`) 📋

Nesta aula aprendi a base da modularização em Python: as funções. Elas permitem isolar blocos de código para serem reutilizados em qualquer parte do programa, evitando a repetição desnecessária (princípio DRY - Don't Repeat Yourself).
In this class, I learned the basis of modularization in Python: functions. They allow isolating blocks of code to be reused anywhere in the program, avoiding unnecessary repetition (DRY principle).

### :clipboard: O que aprendi / What I learned:

* **Definição (`def`):** Usamos a palavra reservada `def` para criar uma função.
* **Parâmetros vs Argumentos:**
    * **Parâmetro:** É o nome definido na criação da função (ex: `nome`).
    * **Argumento:** É o valor real enviado na chamada da função (ex: `'Pedro'`).
* **Retorno Padrão (`None`):** Entendi que toda função no Python retorna algo. Se não especificarmos um `return`, ela devolve automaticamente `None`.
* **Reutilização:** Uma vez definida, a função pode ser executada infinitas vezes com diferentes dados.

---

### 🛠️ Estrutura de uma Função / Function Structure:



| Termo | Descrição | Description |
| :--- | :--- | :--- |
| **`def`** | Inicia a definição da função. | Starts the function definition. |
| **Parâmetros** | Variáveis locais que recebem dados. | Local variables that receive data. |
| **Corpo / Body** | Bloco de código indentado. | Indented block of code. |
| **Chamada / Call** | Execução da função pelo nome. | Executing the function by its name. |

---

### 💡 Insight:
As funções são como "receitas". Você define o passo a passo uma vez e, sempre que precisar daquele prato (resultado), basta chamar a receita pelo nome e passar os ingredientes (argumentos). Isso torna o código muito mais limpo e profissional, seguindo o Zen of Python.