# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

from lista08old.ipc import funcoes

taxa = float(input("Digite o valor da taxa de imposto"))
preco = float(input("Digite o valor do preço"))

total = funcoes.soma_imposto(taxa, preco)

print(total)
