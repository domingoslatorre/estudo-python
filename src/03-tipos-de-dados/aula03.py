""" Aula 03 - Tipos de Dados - Sets """

# set (conjunto)
# não ordenado
# mutáveis
# não indexáveis
# não aceitam elementos duplicados

# criar um set
numeros = {1, 12, 5, 7, 4, 3, 3, 1}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(3 in numeros)
print(50 in numeros)

# adicionar itens no set
print(numeros)
numeros.add(8)
print(numeros)

# adicionar elementos de um set em outro
print('----')
print(numeros)
numeros2 = {1, 5, 4, 4, 3, 11, 9}
print(numeros2)
numeros.update(numeros2)
print(numeros, type(numeros))
