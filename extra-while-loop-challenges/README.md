# Exercícios Extras - Lógica com Loops `WHILE` 🔄

Nesta seção, foquei em laços de repetição que dependem de condições dinâmicas, utilizando o `while` para criar sistemas de interatividade e segurança.

### :clipboard: O que pratiquei:

* **Módulo `random`:** Uso da função `randint(1, 100)` para gerar dados aleatórios, tornando o programa imprevisível e dinâmico.
* **Validação de Entrada:** Uso de blocos `try/except` para garantir que o programa não quebre caso o usuário digite letras onde se esperam números.
* **Contadores:** Implementação de variáveis de incremento (`attempts_counter += 1`) para rastrear o progresso do usuário dentro do laço.
* **Sentinelas e Condições:** Uso de variáveis de controle para manter o loop ativo até que um critério específico (como acertar uma senha) seja satisfeito.

---

### 🛠️ Fluxo de Funcionamento (While Loop):



A diferença crucial entre o `for` e o `while` que pratiquei aqui:
* **For:** Usado quando sabemos (ou temos uma coleção de) quantas vezes vamos repetir.
* **While:** Usado quando a repetição depende de um fator externo (como a vontade do usuário ou um dado aleatório).

| Exercício | Condição de Parada | Ferramenta Chave |
| :--- | :--- | :--- |
| **Adivinhação** | `palpite == secreto` | `random.randint` |
| **Senha** | `palpite == senha` | `while !=` |

---

### 💡 Dica de Ouro (Clean Code):
No exercício da senha, inicializar o palpite como uma string vazia (`""`) garante que ele seja diferente da senha real no primeiro teste, forçando o Python a entrar no loop. É uma técnica elegante para garantir que o código rode ao menos uma vez.