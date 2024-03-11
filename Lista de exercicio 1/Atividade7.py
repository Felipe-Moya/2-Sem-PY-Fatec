h1 = int(input("Qual a idade do primeiro homem? "))
h2 = int(input("Qual a idade do segundo homem? "))
m1 = int(input("Qual a idade da primeira mulher? "))
m2 = int(input("Qual a idade da segunda mulher? "))

hv = max (h1,h2)
hn = min (h1,h2)
mv = max (m1,m2)
mn = min (m1,m2)

soma = hv + mn
produto = hn * mv

print(f"A soma entre as idades do homem mais velho e a mulher mais nova é: {soma}")
print(f"O produto entre as idades do homem mais novo e a mulher mais velha é: {produto}")