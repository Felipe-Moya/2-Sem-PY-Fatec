nconta = int(input("Qual o número da sua conta? "))
saldo = float(input("Qual o saldo da sua conta? "))
debito = float(input("Quanto há de débito em sua conta? "))
credito = float(input("Quanto há de crédito em sua conta? "))

saldot = saldo - (debito + credito)

if saldot >= 0 :
    print("Saldo Positivo")
    print(f"O saldo da conta {nconta} é {saldot:.2f}.")

else:
    print("Saldo Negativo")
    print(f"O saldo da conta {nconta} é {saldot:.2f}.")