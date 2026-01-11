# Aula 82 - Lambdas Avançadas e Closures 🚀

Nesta aula, elevei o nível do uso de funções anônimas, integrando-as com funções de maior ordem e criando fábricas de funções (closures) em apenas uma linha.

### :clipboard: O que aprendi:

* **Lambda como Closure:** Aprendi que uma lambda pode retornar outra lambda. No exemplo `lambda m: lambda n: n * m`, a primeira recebe o multiplicador e a segunda o número, criando um comportamento de "memória" (Closure).
* **Integração com Higher Order Functions:** Usei a função `execute` para processar diferentes lambdas, mostrando a flexibilidade de passar lógica como argumento.
* **Lambdas com *args:** Vi que é possível usar empacotamento de argumentos (`*args`) dentro de uma função anônima para lidar com múltiplos valores dinamicamente.

---

### 🛠️ Visualizando a Lambda Closure:



A estrutura `lambda m: lambda n: n * m` funciona assim:
1. **Pai (`m`):** Recebe o valor (ex: 2) e "congela" esse valor.
2. **Filho (`n`):** É a função que sobra e será executada depois, lembrando que o `m` vale 2.

| Exemplo | Lógica | Resultado |
| :--- | :--- | :--- |
| **Soma** | `lambda x, y: x + y` | Soma simples de dois valores. |
| **Sum Args** | `lambda *args: sum(args)` | Soma de N valores usando built-in. |
| **Factory** | `lambda m: lambda n: n * m` | Cria uma função multiplicadora. |

---

### 💡 Insight:
Embora o exemplo `lambda m: lambda n: n * m` seja tecnicamente elegante, ele pode ser difícil de ler para iniciantes. Em projetos reais, usamos esse nível de abstração para criar pequenos "ajudantes" (helpers) ou em bibliotecas de processamento de dados onde a concisão é valiosa.