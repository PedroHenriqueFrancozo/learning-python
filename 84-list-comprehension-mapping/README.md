# Aula 85 - Mapeamento em List Comprehension 🗺️

Nesta aula, explorei o conceito de **Mapeamento (Mapping)**. No contexto de List Comprehension, mapear significa transformar cada item de uma lista original em um novo valor, resultando em uma nova lista com o mesmo número de elementos.

### :clipboard: O que aprendi:

* **Transformação de Dados:** Como iterar sobre uma lista e aplicar uma modificação (como um cálculo matemático) em cada item individualmente.
* **Uso de Unpacking em Dicionários:** Utilizei `{**product}` para criar uma cópia do dicionário original e alterar apenas a chave necessária (`price`), mantendo a integridade dos outros dados.
* **Mapeamento Condicional:** Aprendi que, ao usar o `if/else` **antes** do `for`, estou realizando um mapeamento. Isso permite decidir qual transformação aplicar a cada item com base em uma condição.

---

### 🛠️ Estrutura do Mapeamento:

No mapeamento, a lógica de decisão vem antes da iteração:
`[ <VALOR_SE_VERDADEIRO> if <CONDICAO> else <VALOR_SE_FALSO> for <ITEM> in <ITERAVEL> ]`

| Conceito | Resultado Esperado |
| :--- | :--- |
| **Mapeamento** | A lista final tem o **mesmo tamanho** da original. |
| **Transformação** | Os valores são alterados conforme a regra definida. |

---

### 💡 Insight:
O mapeamento é essencial quando precisamos "limpar" ou "ajustar" dados vindos de um banco de dados ou API antes de exibi-los ao usuário final, garantindo que todos os itens passem pelo mesmo filtro de regras de negócio.