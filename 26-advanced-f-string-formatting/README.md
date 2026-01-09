# Aula 26 - Formatação Avançada com f-strings 📋

Nesta aula aprendi a utilizar recursos avançados das f-strings para controlar o alinhamento, preenchimento e a exibição de sinais numéricos, tornando a saída de dados muito mais profissional.
In this class, I learned how to use advanced f-string features to control alignment, padding, and numerical signs, making the data output much more professional.

### :clipboard: O que aprendi / What I learned:

* **Alinhamento e Preenchimento:** O uso de `>`, `<`, e `^` para posicionar textos dentro de um espaço definido.
* **Controle de Sinais:** Como forçar a exibição do sinal de positivo `+` em números.
* **Separadores:** O uso da vírgula `,` para separar milhares em números grandes.
* **Conversion Flags:** Aprendi o `!r`, que é excelente para debug, pois mostra o valor "cru" da variável (incluindo as aspas de uma string).
* **Formatação Combinada:** Como unir preenchimento de zeros, sinais e precisão decimal em uma única expressão.

---

### 🛠️ Guia de Alinhamento / Alignment Guide:

| Símbolo | Direção | Exemplo | Resultado (para 'ABC') |
| :---: | :--- | :--- | :--- |
| `>` | Direita | `f'{var:>10}'` | `       ABC` |
| `<` | Esquerda | `f'{var:<10}'` | `ABC       ` |
| `^` | Centro | `f'{var:^10}'` | `   ABC    ` |



---

### 💡 Insight:
O uso do `!r` (repr) é um dos melhores amigos do desenvolvedor. Se você tem uma string que parece vazia, mas na verdade tem um espaço (`' '`), o print normal não mostraria nada, mas o `f'{variavel!r}'` mostraria `' '`, revelando o caractere "invisível" imediatamente.