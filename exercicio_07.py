idades = [22, 15, 30, 17, 18]
idade_valida = [idade for idade in idades if idade >= 18]
print(idade_valida)

idades = [22, 15, 30, 17, 18]
for idade_valida in idades:
    if idade_valida >= 18:
        print(idade_valida)