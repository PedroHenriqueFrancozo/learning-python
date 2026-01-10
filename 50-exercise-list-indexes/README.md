# Aula 50 - Exercício: Exibindo Índices de uma Lista 📋

Nesta aula pratiquei a manipulação de índices de forma manual, utilizando as funções `range` e `len`. Este exercício é fundamental para entender como o Python acessa elementos em coleções.
In this class, I practiced manual index manipulation using the `range` and `len` functions. This exercise is fundamental to understanding how Python accesses elements in collections.

### :clipboard: O que aprendi / What I learned:

* **Função `len()`:** Retorna a quantidade de itens na lista (neste caso, 4).
* **Função `range()`:** Criou uma sequência numérica de `0` até `3` (o `stop` é exclusivo).
* **Acesso por Índice:** Reforcei a sintaxe `lista[indice]` para buscar o valor correspondente a cada posição gerada pelo laço.
* **Inspeção de Tipos:** Usei o `type()` para confirmar que, embora a lista seja um objeto único, cada elemento dentro dela mantém seu próprio tipo de dado original.

---

### 🛠️ Lógica do Exercício / Exercise Logic:

[Image showing a list linked to a range sequence]

| Índice (range) | Valor (lista) | Tipo |
| :--- | :--- | :--- |
| 0 | 'Maria' | `<class 'str'>` |
| 1 | 'Helena' | `<class 'str'>` |
| 2 | 'Luiz' | `<class 'str'>` |
| 3 | 'João' | `<class 'class 'str'>` |

---

### 💡 Insight:
Embora o `enumerate` (que vimos na aula 53) seja mais prático, dominar o `range(len(lista))` é vital. Existem situações onde você precisa manipular o índice de forma mais complexa (como pular itens ou comparar o item atual com o próximo `lista[i+1]`), e para esses casos, essa lógica manual é a ferramenta correta.