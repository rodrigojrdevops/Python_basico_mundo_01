numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('analisando o número {}'.format(numero))
print('A unidade: {}'.format(u))
print('A dezena: {}'.format(d))
print('A centena: {}'.format(c))
print('A milhar: {}'.format(m))
