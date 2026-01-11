# Aula 80 - Exercício: Primeiro Número Duplicado 🔢

Nesta aula, o desafio foi criar um algoritmo capaz de identificar o primeiro número a se repetir em uma sequência. A regra principal é: o "vencedor" é aquele cuja **segunda ocorrência** aparece primeiro no código.

### :clipboard: Explicação da Lógica:

Para resolver este problema de forma eficiente, utilizei a estrutura de dados **Set** (Conjunto):

1. **Memória de Curto Prazo:** Criamos um set vazio chamado `checked_numbers`.
2. **Varredura:** Iteramos sobre a lista número por número.
3. **Verificação de Existência:** * Se o número **já estiver** no set, significa que encontramos sua segunda ocorrência. Retornamos ele imediatamente.
    * Se **não estiver**, adicionamos o número ao set e passamos para o próximo.
4. **Caso Negativo:** Se o loop terminar sem encontrar duplicatas, retornamos `-1`.

---

### 🛠️ Por que usar Set e não Lista?



| Estrutura | Verificação (`in`) | Motivo |
| :--- | :--- | :--- |
| **Lista** | Lenta | Precisa percorrer todos os itens até achar (ou não) o valor. |
| **Set** | **Instantânea** | Usa uma Tabela Hash, indo direto ao endereço do valor na memória. |

### 💡 Exemplo de Fluxo:
Lista: `[1, 4, 9, 8, 9, 4]`
- Encontra `1`: Set `{1}`
- Encontra `4`: Set `{1, 4}`
- Encontra `9`: Set `{1, 4, 9}`
- Encontra `8`: Set `{1, 4, 9, 8}`
- Encontra `9`: **Opa!** Já está no Set. Retorna `9`.