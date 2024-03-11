ht = int(input("Quantas horas você trabalhou? "))
salario = 1200.00

if ht > 40:
    ht -= 40
    bonif = ((salario / 160) * 1.5) * ht + salario
    print(f"Foi adicionada a bonificação. Seu salario foi: R$:{bonif:.2f}.")

else:
    print(f"Seu salario foi: R$:{salario:.2f}.")