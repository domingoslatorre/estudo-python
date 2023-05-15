""" Aula 01 - Introdução a funções """

# Função é um bloco que realiza uma tarefa específica
# Dividir o problema em pequenas parte
# Evitar duplicação de código

# 1. Standard Library Functions - built-in functions
# ex: print, len

print('Olá', 123, True)

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)


# 2. User Defined Functions
# Definidas pelo desenvolvedor(a)
# Fazerem parte da solução do problema

# Declaração
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum
def saudacoes():
    print('Olá')


# Chamada
saudacoes()
saudacoes()
saudacoes()


# Declaração
# nome: saudacoes
# parametros: nome
# retorno: nenhum
def saudacoes(nome):
    print(f'Olá {nome}')


# Chamada
# valores, variáveis, expressoes => argumentos
# 'Maria' é um argumento passado para o parâmetro nome
saudacoes('Maria')
saudacoes('Pedro')
nome = 'Carlos'
saudacoes(nome)

# Declaração
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: nenhum


def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)


# Chamada
# argumentos são literais
calcular_media(10.0, 3.0, 6.0)

n1 = 10.0
n2 = 3.0
n3 = 8.0
# argumentos são variáveis
calcular_media(n1, n2, n3)


# Declaração
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: media
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


media = calcular_media(10.0, 8.4, 3.2)
print('valor da média', media)
# enviar no email
# salvar no bancod e dados
# salvar no arquivo
