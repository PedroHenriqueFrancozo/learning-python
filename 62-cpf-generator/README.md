# Aula 62 - Gerador de CPFs Aleatórios 🎲

Nesta aula utilizei a lógica de validação desenvolvida anteriormente para criar um script capaz de gerar CPFs válidos matematicamente.
In this class, I used the validation logic developed previously to create a script capable of generating mathematically valid CPFs.

### :clipboard: O que aprendi / What I learned:

* **Módulo `random`:** Uso da função `random.randint(0, 9)` para gerar números aleatórios.
* **Automação de Testes:** Agora posso gerar milhares de CPFs para testar o validador da Aula 61.
* **Inversão de Lógica:** Em vez de receber e validar, o programa agora cria a base e calcula os complementos necessários.

---

### 💡 Insight:
Um gerador de dados (faker) é essencial para testes automatizados. Em sistemas reais, nunca usamos dados reais de pessoas para testes; criamos geradores como este para garantir a segurança da informação.