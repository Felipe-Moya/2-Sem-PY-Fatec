nota1 = float(input("Qual foi a nota da Primeira fase? "))
nota2 = float(input("Qual foi a nota da Segunda fase? "))

result = (nota1 + nota2) / 2.0

if result >= 8:
    print(f"Sua experiência foi boa {result:.2f}.")

else:
    print(f"Sua experiência foi regular {result:.2f}.")