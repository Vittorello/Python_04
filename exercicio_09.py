valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [par for par in valores if par % 2==0]
impares = [impar for impar in valores if impar % 2!=0]

print(pares)
print(impares)