# Aula 76 - Dicionários em Python (`dict`) 📖

Nesta aula explorei profundamente os dicionários, que são estruturas de dados baseadas em pares de **Chave e Valor**. Eles são fundamentais para organizar dados de forma nomeada, funcionando de forma similar a objetos em outras linguagens.
In this class, I deeply explored dictionaries, which are data structures based on **Key and Value** pairs. They are essential for organizing named data, working similarly to objects in other languages.

### :clipboard: Enunciados e Conceitos / Topics Covered:

* **Estrutura Base:** Chaves devem ser tipos imutáveis (`str`, `int`, `tuple`), enquanto valores podem ser qualquer coisa.
* **Manipulação:** Como criar, editar e deletar (`del`) chaves dinamicamente.
* **Método `.get()`:** Uma forma segura de acessar valores sem interromper o programa caso a chave não exista.
* **Shallow Copy (`.copy()`):** Entendi que cópias rasas não duplicam objetos mutáveis (como listas) dentro do dicionário. Para uma cópia total, usamos `copy.deepcopy()`.
* **Método `.update()`:** Permite fundir dois dicionários ou atualizar valores existentes de várias formas (dicionário, tuplas ou listas).

---

### 🛠️ Métodos Úteis / Useful Methods:



| Método | Descrição | Description |
| :--- | :--- | :--- |
| `keys()` | Retorna as chaves do dicionário. | Returns dictionary keys. |
| `values()` | Retorna os valores. | Returns the values. |
| `items()` | Retorna pares (chave, valor). | Returns (key, value) pairs. |
| `setdefault()` | Garante um valor padrão. | Sets a default value if key is missing. |
| `pop()` | Remove e retorna um item específico. | Removes and returns a specific item. |

---

### 💡 Insight:
O método `.update()` é extremamente versátil. Ele não apenas aceita outro dicionário, mas também qualquer iterável que se comporte como pares (como uma lista de listas ou uma lista de tuplas). Isso facilita muito a conversão de dados de diferentes fontes para dentro do seu objeto principal.