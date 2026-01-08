import math

num = float(input(f"Digite um número real: ").replace(',', '.')) 

print('o valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
