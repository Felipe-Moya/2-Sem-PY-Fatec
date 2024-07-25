cpf = input("Digite seu CPF: ")
D1 = 11 - (((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[3]) * 7) + (int(cpf[4]) * 6) + (int(cpf[5]) * 5) + (int(cpf[6]) * 4) + (int(cpf[7]) * 3) + (int(cpf[8]) * 2)) % 11)

if D1 == int(cpf[9]):
    D2 = 11 - (((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[3]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[7]) * 4) + (int(cpf[8]) * 3) + (int(cpf[9]) * 2)) % 11)
    if D2 >= 10:
        D2 = 0
    if D2 == int(cpf[10]):
        print("CPF Valido")
    else:
        print("CPF invalido... Digite um valido")

else:
    print("CPF invalido... Digite um valido")