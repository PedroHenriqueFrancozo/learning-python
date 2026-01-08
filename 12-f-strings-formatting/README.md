# Aula 13 - Formatação com F-Strings 📋

Nesta aula aprendi a usar **f-strings**, a maneira mais moderna e eficiente de formatar textos no Python.
In this class, I learned how to use **f-strings**, the most modern and efficient way to format text in Python.

### :clipboard: O que aprendi / What I learned:

* **Interpolação de Variáveis:** Inserir variáveis diretamente dentro de uma string usando `{}`.
* **Formatação Numérica (`:.2f`):** Como limitar o número de casas decimais (ex: transformar `20.9876` em `20.99`).
* **Praticidade:** As f-strings facilitam a leitura do código em comparação com a concatenação comum.

---

### 🛠️ Exemplo de Formatação / Formatting Example:

| Código | Resultado Esperado | Explicação |
| :--- | :--- | :--- |
| `{var:.1f}` | `20.9` | 1 casa decimal |
| `{var:.2f}` | `20.99` | 2 casas decimais |
| `{var:,.2f}` | `1,000.50` | Com vírgula de milhar |

---
### 💡 Insight:
O `f` antes das aspas diz ao Python: "Ei, fique atento, pois vou colocar variáveis aqui dentro!". É muito mais limpo que usar o sinal de `+`.