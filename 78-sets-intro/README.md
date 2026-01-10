# Aula 78 - Sets em Python (`set`) 集合

Nesta aula aprendi sobre os Conjuntos (Sets), uma estrutura de dados focada em performance e unicidade. Eles são ideais para quando não precisamos nos preocupar com a ordem, mas sim com a existência do item.
In this class, I learned about Sets, a data structure focused on performance and uniqueness. They are ideal when we don't care about order, but rather about the item's existence.

### :clipboard: O que aprendi / What I learned:

* **Unicidade:** Sets removem automaticamente valores duplicados. Útil para "limpar" listas. / Sets automatically remove duplicate values. Useful for "cleaning" lists.
* **Tipos Aceitos:** Apenas tipos imutáveis (`str`, `int`, `tuple`) podem estar dentro de um set.
* **Performance:** Verificar se um item está em um set (`in`) é muito mais rápido do que em uma lista.
* **Sem Ordem:** Diferente das listas e dicionários (em versões recentes), os sets não mantêm a ordem de inserção.

---

### 🛠️ Comparação de Coleções / Collection Comparison:



| Tipo | Ordenado? | Mutável? | Duplicatas? |
| :--- | :--- | :--- | :--- |
| **List** | Sim | Sim | Sim |
| **Tuple** | Sim | Não | Sim |
| **Set** | Não | Sim | **Não** |

---

### 💡 Insight:
Uma das aplicações mais comuns dos sets no dia a dia é a remoção de duplicatas de uma lista. Basta fazer `lista = list(set(lista))`. Porém, lembre-se: ao fazer isso, você perderá a ordem original dos elementos!