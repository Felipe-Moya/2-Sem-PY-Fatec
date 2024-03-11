salario = 1200.00
totalv = float(input("Qual foi o valor total de vendas efetuadas esse mês? "))

salariob = totalv * 0.03 + salario

if totalv > 20000.00:
    salariob += 600
    print("Atingiu a Meta")
    print(f"Seu salario total foi: {salariob:.2f}.")

else:
     print(f"Seu salario foi: {salariob:.2f}.")