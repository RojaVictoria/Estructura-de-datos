import sys

sol_peruano = sys.argv[1]
peso_argentino = sys.argv[2]
dolar_americano = sys.argv[3]
valor_peso_chileno = sys.argv[4]

sol_convertido = float(sol_peruano) * int(valor_peso_chileno)
peso_arg_convertido = float(peso_argentino) * int(valor_peso_chileno)
dolar_convertido = float(dolar_americano) * int(valor_peso_chileno)

print(f'Los {valor_peso_chileno} pesos equivalen a:')
print(f'{sol_convertido} Soles')
print(f'{peso_arg_convertido} Pesos Argentinos')
print(f'{dolar_convertido} Dólares')