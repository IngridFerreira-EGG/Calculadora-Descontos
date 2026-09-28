#Entrada de valores
valor_total_compra = float(input("Valor da compra: "))

#Processamento do desconto a aplicar
if valor_total_compra < 200.00:
    desconto1 = (valor_total_compra * 0.05)
elif valor_total_compra >= 200.00:
    desconto2 = (valor_total_compra * 0.1)
elif valor_total_compra >= 300.00:
    desconto3 = (valor_total_compra * 0.15)

#Saída do valor final com o desconto aplicado
if desconto1:
    print("Você ganhou um desconto de 5%. O valor da sua compra após o desconto é de {desconto1} reais")
elif desconto2:
    print("Você ganhou um desconto de 10%. O valor da sua compra após o desconto é de {desconto2} reais")
elif desconto3:
    print("Você ganhou um desconto de 15%. O valor da suacompra após o desconto é de {desconto3} reais")