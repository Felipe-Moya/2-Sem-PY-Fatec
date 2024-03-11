from hashlib import sha256

cont = 0
tentativas = 2

# A senha é abc123
senha_ok = "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"

while True:
    login = input("Login: ")
    senha = input("Senha: ")
    senha_hash = sha256(senha.encode('utf-8')).hexdigest()
    print("")
          
    if login == "ABC" and senha_hash == senha_ok:
        print("Acesso permitido!")
        break

    elif senha_hash != senha_ok and cont < 2:
        print(f"Acesso negado, mais {tentativas} tentativas!")
        print("")
        cont += 1
        tentativas -= 1

    else:
        print("Excedeu o número de tentativas.")
        break

quit()