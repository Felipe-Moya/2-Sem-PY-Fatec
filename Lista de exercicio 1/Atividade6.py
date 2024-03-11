litros = float(input("Quantos litros foram vendidos? "))
tipo = input("Qual o tipo de combustível? ").upper()[0]

if tipo == "G":
    result = 4.90 * litros
    print(f"O valor a ser pago é R$: {result:.2f}.")
    
if tipo == "A":
    result = 3.90 * litros
    print(f"O valor a ser pago é R$: {result:.2f}.")

if tipo == "D":
    result = 5.90 * litros
    print(f"O valor a ser pago é R$: {result:.2f}.")

else:
    print("Erro.")