# DIO - Potência Tech powered by IFood - Ciências de Dados com Python
# DESAFIO: Gerenciamento de Pedidos de Comida Online

""" DESCRIÇÃO DO DESAFIO:
Você foi contratado para desenvolver um sistema que armazena informações dos pedidos de comida online realizados por um cliente. O sistema deve permitir ao cliente inserir novos pedidos, escolher um cupom de desconto (10% ou 20%) e exibir o valor total de todos os pedidos realizados até o momento, com o desconto aplicado.

Entrada
A entrada é composta por:
Uma linha com um número inteiro n representando a quantidade de pedidos que o usuário deseja inserir;
n linhas, cada uma contendo uma string com o nome do pedido e um valor em ponto flutuante separados por espaço. O nome do pedido não contém espaços em branco;
Uma linha contendo o cupom de desconto escolhido (10% ou 20%).

Saída
O programa deve exibir uma única linha contendo o valor total de todos os pedidos com o desconto aplicado, no seguinte formato:

Valor total: XX.YY, onde "XX.YY" é a soma de todos os pedidos com desconto em formato de duas casas decimais após a vírgula.

"""


def main():
    n = int(input("Digite a quantidade de pedidos: "))
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input("Digite o pedido (item e valor (Pizza 35.50)): ").split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
# TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).

    desconto = input("\nDigite o desconto (10% ou 20%): ")

    if desconto == "10%":
        total *= 0.9
        print(f"\nValor total: {total:.2f}\n")
    elif desconto == "20%":
        total *= 0.8
        print(f"\nValor total: {total:.2f}\n")
 
if __name__ == "__main__":
    main()

# RESPOSTA NA PLATAFORMA DO DESAFIO:
"""
    desconto = input()

    if desconto == "10%":
        total *= 0.9
        print(f"Valor total: {total:.2f}")
    elif desconto == "20%":
        total *= 0.8
        print(f"Valor total: {total:.2f}")

 
if __name__ == "__main__":
    main() 
    
"""