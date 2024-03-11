qnta = int(input("Qual a quantidade atual do pruduto no estoque? "))
qntmax = int(input("Qual a quantidade máxima de produtos no estoque? "))
qntmin = int(input("Qual a quantidade minima de produtos no estoque? "))

qntmed = (qntmax + qntmin) // 2
print("A quantidade média do estoque é:", qntmed)

if qnta >= qntmed:
    print("Não efetuar compra.")
    
else:
    print("Efetuar compra.")