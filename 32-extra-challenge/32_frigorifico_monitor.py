# Desafio: Sistema de Alerta de Frigorífico
# O Cenário: Você precisa monitorar a temperatura de um caminhão que transporta vacinas. As vacinas devem ser mantidas entre 2°C e 8°C.

# O que o programa deve fazer:
# Entrada de Dados: Peça ao usuário para digitar a temperatura atual (aceite números decimais).

# Validação Robusta:
# Use try/except para garantir que o usuário digite um número.

# Se for um erro, exiba uma mensagem de alerta e encerre o programa amigavelmente.
# Lógica de Negócio (Use Constantes):

# Defina TEMP_MIN = 2.0 e TEMP_MAX = 8.0.

# Crie variáveis booleanas (flags) para: esta_congelando, esta_superaquecendo e temperatura_ideal.

# Data e Hora: * Se a temperatura estiver fora do intervalo (ideal é False), use o módulo datetime para exibir o horário exato do alerta no formato: "ALERTA EMITIDO EM: HH:MM:SS".

# Extra (Slicing/Formatting):
# Exiba a temperatura com apenas 1 casa decimal.
# Se o usuário digitar uma temperatura com sinal (ex: +5.0 ou -2.0), use f-string para garantir que o sinal sempre apareça na saída final (f'{valor:+}').