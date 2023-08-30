# DIO - Potência Tech powered by IFood - Ciências de Dados com Python
# DESAFIO: Calcular o Preço Final de um Pedido

""" DESCRIÇÃO DO DESAFIO:
Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.

Entrada:
A entrada deve receber os valores abaixo:

valorHamburguer: o valor unitário de um hambúrguer.
quantidadeHamburguer: a quantidade de hambúrgueres que o usuário deseja.
valorBebida: o valor unitário de uma bebida.
quantidadeBebida: a quantidade de bebidas que o usuário deseja.
valorPago: o valor pago pelo usuário.

Saída:
A saída deve retornar um texto informando o valor total do pedido e a quantidade de troco que será necessário. Por exemplo, se tivermos os seguintes valores de entrada:

valorHamburguer = 10.00;
quantidadeHamburguer = 2;
valorBebida = 5.00;
quantidadeBebida = 1;
valorPago = 30.00;
De acordo com esses valores de entrada, o cálculo do preço final do pedido ficaria assim:

Valor total dos hambúrgueres: 10.00 * 2 = 20.00
Valor total da bebida: 5.00 * 1 = 5.00
Preço total do pedido: 20.00 + 5.00 = 25.00
Troco necessário: 30.00 - 25.00 = 5.00
Como o usuário pagou R$ 30.00 e o preço total do pedido ficou em R$ 25.00, o troco necessário é de R$ 5.00. Portanto, a saída esperada para esse exemplo seria:

O preço final do pedido é R$ 25.00. Seu troco é R$ 5.00.

"""


valorHamburguer = float(input("\nInsira o valor unitário de um hambúrguer: R$"))
quantidadeHamburguer = int(input("Insira a quantidade de hambúrgueres desejada: "))
valorBebida = float(input("Insira o valor unitário de uma bebida: R$"))
quantidadeBebida = int(input("Insira a quantidade de bebidas: "))
valorPago = float(input("\nInsira o valor pago pelo usuário: R$"))

# TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

precoHamburguer = valorHamburguer * quantidadeHamburguer
precoBebida = valorBebida * quantidadeBebida
precoFinal = precoHamburguer + precoBebida

# TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

trocoPedido = valorPago - precoFinal

# TODO: Imprimir a saída no formato especificado neste desafio.

print(f"\nA pagar: R$ {precoFinal:.2f}")
print(f"Dinheiro recebido: R$ {valorPago:.2f}")

if valorPago < precoFinal:
    valorFaltante = - (valorPago - precoFinal)

    print(f"Valor insuficiente! Complete com R$ {valorFaltante:.2f}\n")

else:
    print(f"Troco: R$ {trocoPedido:.2f}\n")
    
# RESPOSTA NA PLATAFORMA DO DESAFIO:

# print(f"O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {trocoPedido:.2f}.")