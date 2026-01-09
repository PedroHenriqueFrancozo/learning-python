# Aula 28 - Exercício: Análise de Texto e Lógica 📋

Nesta aula, realizei um exercício prático para integrar conhecimentos de fatiamento de strings, verificação de condições e manipulação de índices. O objetivo foi criar um programa que analisa o nome e a idade do usuário.
In this class, I completed a practical exercise to integrate knowledge of string slicing, condition checking, and index manipulation. The goal was to create a program that analyzes the user's name and age.

### :clipboard: O que apliquei / What I applied:

* **Validação de Presença:** O uso de `if nome and idade` para verificar se as strings não estão vazias (**Falsy**).
* **Fatiamento Dinâmico:** Inversão de string com `[::-1]`.
* **Busca em Iteráveis:** O operador `in` para detectar espaços em branco.
* **Acesso por Índice:** Identificação da primeira (`[0]`) e da última (`[-1]`) letra de forma direta.
* **Medição:** Uso da função `len()` para calcular o tamanho total do texto.

---

### 🛠️ Resultado da Análise / Analysis Result:

| Teste | Função/Lógica | Exemplo de Saída |
| :--- | :--- | :--- |
| **Inversão** | `[::-1]` | `oizuL` |
| **Presença de Espaço** | `' ' in nome` | `Contém espaços` |
| **Contagem** | `len(nome)` | `5` |
| **Último Caractere** | `nome[-1]` | `z` |

---


### 💡 Insight:
Este exercício mostra a importância da ordem das verificações. Ao testar primeiro `if nome and idade`, garantimos que o programa não tente acessar índices de uma string vazia (como `nome[0]`), o que causaria um erro de `IndexError`. A lógica de programação também envolve prevenir que o programa quebre com entradas inesperadas.