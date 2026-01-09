# Aula 25 - Interpolação Básica de Strings 📋

Nesta aula aprendi a técnica de interpolação de strings usando o operador `%`. Embora as f-strings sejam mais modernas, a interpolação é essencial para entender códigos legados e para trabalhar com bases numéricas como Hexadecimal.
In this class, I learned the string interpolation technique using the `%` operator. While f-strings are more modern, interpolation is essential for understanding legacy code and working with numerical bases like Hexadecimal.

### :clipboard: O que aprendi / What I learned:

* **Marcadores de Tipo:** Aprendi os principais placeholders: `%s` para strings, `%d` para inteiros e `%f` para decimais.
* **Precisão de Floats:** Como limitar casas decimais (ex: `%.2f`).
* **Conversão Hexadecimal:** O uso de `%x` ou `%X` para converter números decimais em hexadecimais.
* **Preenchimento (Padding):** O uso de `%08X` para garantir que o resultado tenha 8 dígitos, preenchendo com zeros à esquerda se necessário.

---

### 🛠️ Tabela de Referência / Reference Table:

| Marcador | Tipo de Dado | Exemplo |
| :--- | :--- | :--- |
| `%s` | String | `"%s" % "Oi"` |
| `%d` ou `%i` | Inteiro | `"%d" % 10` |
| `%f` | Float | `"%.2f" % 1.50` |
| `%x` / `%X` | Hexadecimal | `"%X" % 255` (FF) |



---

### 💡 Insight:
A interpolação é especialmente útil quando você precisa de formatações técnicas. Por exemplo, `%04d` transformaria o número `7` em `0007`. É uma ferramenta de precisão muito robusta para logs e sistemas que exigem padrões fixos de caracteres.