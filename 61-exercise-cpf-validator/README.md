# Aula 61 - Exercício: Validador de CPF 📋

Nesta aula, implementei um algoritmo completo para validar CPFs brasileiros. O desafio envolveu a limpeza de dados, cálculos matemáticos específicos para os dígitos verificadores e o tratamento de casos de erro.
In this class, I implemented a complete algorithm to validate Brazilian CPFs. The challenge involved data cleaning, specific mathematical calculations for verifier digits, and error handling.

### :clipboard: O que aprendi / What I learned:

* **Limpeza de Dados (Data Cleaning):** Como extrair apenas números de uma string usando `isdigit()`.
* **Algoritmo de Verificação:** Entendi a lógica de pesos regressivos (10 a 2 e 11 a 2) usada para calcular os dígitos oficiais.
* **Módulo `sys`:** Uso do `sys.exit()` para interromper a execução do programa em casos de dados inválidos (como sequências repetidas).
* **Reforço de Tipos:** A necessidade constante de converter `str` para `int` para realizar os cálculos e voltar para `str` para concatenar o CPF final.

---

### 🛠️ Lógica do Cálculo / Calculation Logic:

| Passo | Descrição | Descripiton |
| :--- | :--- | :--- |
| **1** | Pegar os 9 primeiros dígitos. | Get the first 9 digits. |
| **2** | Multiplicar por pesos de 10 a 2. | Multiply by weights from 10 to 2. |
| **3** | Calcular o resto da divisão por 11. | Calculate the remainder of division by 11. |
| **4** | Repetir para o 2º dígito (pesos 11 a 2). | Repeat for the 2nd digit (weights 11 to 2). |

---

### 💡 Insight:
Validar um CPF não é apenas verificar se ele tem 11 números. O cálculo dos dígitos verificadores garante que o número segue uma estrutura matemática correta. Além disso, aprendi que CPFs com números todos iguais (ex: 111.111.111-11) passam no cálculo matemático, mas são considerados inválidos pela Receita Federal, por isso a importância da verificação de sequência.