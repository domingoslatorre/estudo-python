""" Aula 01 - Operadores """

# Operadores Aritméticos
n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.5

print('1 + 1', 1 + 1, type(1+1))
print('1.2 + 1.3', 1.2 + 1.3, type(1.2+1.3))
print('resultado', resultado, type(resultado))
print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3 % 2)
print(10 // 3)
print(10 ** 3)

# Operador de atribuição
x = 10.0
print(x)

# Operadores de comparação
resultado = x > 10
print(resultado, type(resultado))

print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 < 10', 10 < 10, type(10 < 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))


# condicao = x > 10.0 and resultado < 3.0
# if condicao:
#     pass

# Operadore lógicos
print('True and True', True and True, type(True and True))
print('True and False', True and False, type(True and False))
print('False and True', False and True, type(False and True))
print('False and False', False and False, type(False and False))

print('True or True', True or True, type(True or True))
print('True or False', True or False, type(True or False))
print('False or True', False or True, type(False or True))
print('False or False', False or False, type(False or False))

condicao = False
print('not condicao', not condicao, type(not condicao))


# Operadores especiais

# is
# == comparar se dois valores são iguais
# is verificar se as variáveis apontam para o mesmo
# objeto em memória

a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c)

# in
# str, list, tuple, set, dic (chave)

frase = 'Você é um palavrao!'

print('palavrao' in frase, type('palavrao' in frase))
print('Palavrao' in frase, type('Palavrao' in frase))

numeros = {1, 5, 2, 6}
print(1 in numeros)

pessoa = {
    'nome': 'Maria',
    'idade': 22,
    'email': 'maria@email.com'
}

print(22 in pessoa)
