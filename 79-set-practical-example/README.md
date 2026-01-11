# Aula 79 - Uso Prático de Sets 🚀

Nesta aula, apliquei os conceitos de Conjuntos (Sets) em um loop de entrada prático. Isso demonstra como os sets são usados para "lembrar" dados e realizar buscas rápidas.

### :clipboard: O que aprendi:

* **Crescimento Dinâmico:** Sets são mutáveis, então podemos usar o método `.add()` para expandir a coleção conforme o programa executa.
* **Busca Eficiente:** O uso de `if 'l' in letras` é a forma mais performática no Python para verificar se um item existe em uma coleção.
* **Normalização de Dados:** Ao usar `.lower()`, garantimos que 'L' e 'l' sejam tratados como o mesmo elemento, evitando erros na lógica dependendo da entrada do usuário.

---

### 🛠️ Insight de Performance:



Em uma **Lista**, o computador verifica os itens um por um. Em um **Set**, ele utiliza uma "Tabela Hash", que permite encontrar o item quase instantaneamente, mesmo que o conjunto tenha milhões de elementos.

| Comparação | Busca em Lista | Busca em Set |
| :--- | :--- | :--- |
| **Lógica** | Busca Linear | Busca por Hash |
| **Eficiência** | O(n) - Fica lento conforme cresce | O(1) - Velocidade constante |

---

### 💡 Insight:
Esta lógica é a base para muitas ferramentas profissionais, como **contadores de visitantes únicos** em sites ou **filtros de spam** que verificam se uma palavra pertence a um conjunto de termos "bloqueados".