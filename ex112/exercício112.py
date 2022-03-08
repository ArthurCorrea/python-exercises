from ex112.utilidadesCev import moeda
from ex112.utilidadesCev import dado

n = dado.leiaDinheiro('Digite um valor: R$')
moeda.resumo(n, float(input('Quantos % de aumento? ')), float(input('E de redução? ')))

