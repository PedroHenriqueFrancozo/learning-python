# Estudo Extra - Domínio de Dicionários 📚

Este arquivo é um guia prático que criei para consolidar o conhecimento sobre dicionários em Python, cobrindo desde o acesso básico até a manipulação de dados aninhados (Nested Dictionaries).

### :clipboard: O que aprendi e pratiquei:

* **Conceito de Chave/Valor:** Assim como um dicionário de papel, o Python associa uma chave única a um valor.
* **Dicionários Aninhados:** Como acessar dados em "camadas". Ex: `estoque['Maçã']['preço']`.
* **Métodos Fundamentais:**
    * `.keys()`: Lista as chaves.
    * `.values()`: Lista os valores.
    * `.items()`: Retorna pares chave-valor (ideal para loops `for`).
    * `.get()`: Acesso seguro que evita o erro `KeyError` se a chave não existir.
* **Manipulação (CRUD):** Criar, Ler, Atualizar e Deletar itens de uma coleção.

---

### 🛠️ Comparação de Estruturas:



| Estrutura | Quando usar? | Exemplo |
| :--- | :--- | :--- |
| **Dict Simples** | Dados diretos. | `{'nome': 'Ana'}` |
| **Dict Aninhado** | Dados complexos e categorizados. | `{'Maçã': {'preco': 10}}` |
| **Lista de Dicts** | Coleção de itens independentes. | `[{'item': 'A'}, {'item': 'B'}]` |

---

### 💡 Dicas de Formatação e Busca:

1.  **Alinhamento no Print:** Use `: <10` para alinhar à esquerda ou `: >10` para a direita, deixando seus relatórios com colunas perfeitas.
2.  **Busca com `.strip()`:** Sempre use `.strip()` em inputs de usuário para remover espaços acidentais que podem quebrar a lógica de comparação.
3.  **Segurança com `.get()`:** Definir um valor padrão no `.get(busca, "Não encontrado")` torna o programa muito mais robusto e amigável.