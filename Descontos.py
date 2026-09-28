#Entrada de valores
valor_total_compra = float(input("Valor da compra: "))

#Processamento do desconto a aplicar
if valor_total_compra >= 300.00:
    desconto = (valor_total_compra * 0.15)
    percentual = "15%"
elif valor_total_compra >= 200.00:
    desconto = (valor_total_compra * 0.1)
    percentual = "10%"
else:
    desconto = (valor_total_compra * 0.05)
    percentual = "5%"

#Cálculo do valor final da compra após o desconto
valor_final = valor_total_compra - desconto

#Saída do valor final com o desconto aplicado
print(f"Você ganhou um desconto de {percentual}. O valor da sua compra após o desconto é de {valor_final} reais ")
