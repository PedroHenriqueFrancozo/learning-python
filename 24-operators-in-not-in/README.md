# Aula 24 - Operadores `in` e `not in` 📋

Nesta aula aprendi como verificar a presença (ou ausência) de uma fatia de texto dentro de uma string. Strings em Python são **iteráveis**, o que significa que podemos navegar por cada caractere individualmente através de índices.
In this class, I learned how to check for the presence (or absence) of a text snippet within a string. Strings in Python are **iterables**, meaning we can navigate through each individual character using indexes.

### :clipboard: O que aprendi / What I learned:

* **Iteráveis:** Entendi que strings podem ser acessadas caractere por caractere via índices (positivos e negativos).
* **Operador `in`:** Retorna `True` se o valor procurado estiver presente na sequência.
* **Operador `not in`:** Retorna `True` se o valor procurado **não** estiver presente na sequência.
* **Índices:** A contagem começa em `0` para a frente e em `-1` para começar de trás para frente.

---

### 🛠️ Exemplo de Indexação / Indexing Example:

| O | t | á | v | i | o |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 2 | 3 | 4 | 5 |
| -6 | -5 | -4 | -3 | -2 | -1 |



---

### 💡 Insight:
Os operadores `in` e `not in` são o que chamamos de "Pythonic". Em outras linguagens, você precisaria usar funções complexas para encontrar uma substring. Em Python, a leitura é quase como ler um texto em inglês: `if "a" in "casa":` (Se "a" está em "casa"). Isso torna o código muito mais fácil de manter e entender.

commit - feat: add operators in and not in with string indexing study