""" Aula 01 - Tipos de Dados - Listas """

# lista
# ordenadas
# mutáveis
# indexáveis

# criação da lista
nomes = ['Maria', 'Pedro', 'João']
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)


# tamanho de uma lista
# função len
tamanho = len(nomes)
print(tamanho)

# adicionar elementos na lista
# método append
nomes.append('Marta Gomes')
print(nomes)

# método insert
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Lucia')
print(nomes)

# método extend
nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos

# método remove

nomes.remove('Maria da Silva')
print(nomes)

# del

del nomes[0]
print(nomes)

# remove da memória
# del nomes
print(nomes)

# limpar a lista
# método clear
# nomes.clear()
print(nomes)


# iteração em lista
for nome in nomes:
    print(nome)

print('----')

for i in range(len(nomes)):
    print(nomes[i])
