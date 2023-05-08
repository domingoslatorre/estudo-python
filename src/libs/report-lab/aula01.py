""" Aula 01 - Report Lab - Canvas """

# criar o virtual evn
# python -m venv venv

# ativar o venv
# bash
# source ./venv/Scripts/activate

# powershell
# Set-ExecutionPolicy AllSigned (como admin)
# ./venv/Scripts/Activate.ps1


# instalar a lib reportlab
# pip install reportlab

# gerar o arquivo requirements.txt
# pip freeze > requirements.txt


from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, mm, cm, pica
from reportlab.pdfgen import canvas

# letter 612, 792 points (não é pixel, nem milimetros)
print(letter, type(letter))
# A4 595, 841
print(A4, type(A4))

# ponto é uma unidade de medida utilizada para especificar
# tamanho, posição e outras dimensões dos elementos
# de um documento, como texto, imagens, margens, espaçamentos

# inch = polegada
# pica =

# 1 point é aproximadamente:
print(inch, mm, cm, pica)


# Objeto canvas
# pdfgen package
# colocar no .gitignore *.pdf
# instalar o adobe acrobat reader para facilitar (sem complementos de macafee) https://get.adobe.com/br/reader/
# a visualização/atualização do documento
canvas1 = canvas.Canvas('hello-world.pdf')

# origin (0,0) bottom/left
canvas1.drawString(0, 0, 'Hello World!!!')
canvas1.showPage()  # salva a página atual no canvas

# canvas.drawString(0, 0, 'Hello World 2!!!')
# canvas.showPage() # salva uma segunda página no canvas

canvas1.save()  # salva o documento em disco


# TODO: Ver o que o construtor do Canvas recebe como argumentos


# reportlab posiciona os elementos usando pontos
# podemos escrever uma funcao que converte pontos
# para a unidade específica

# qualquer unidade
# inicia no top left, usando a altura para trocar o y de bottom para top
def coord(x, y, height, unit=1):
    """ coordenada x, y, a altura da página e unidade"""
    x, y = x * unit, height - y * unit
    return x, y


def coord2(x, y, unit=1):
    """ coordenada x, y, unidade"""
    x = x * unit
    y = y * unit
    return x, y


canvas2 = canvas.Canvas('documento2.pdf', pagesize=letter)
width, height = letter

# 10mm left and 50mm top
canvas2.drawString(*coord(10, 50, height, mm), text="texto do documento 2")
canvas2.drawString(*coord2(10, 50, mm), text="Olá Olá")

canvas2.showPage()
canvas2.save()


# Canvas métodos

# setFont - PostScript font - fonte vetorial escaláveis
# usadas em várias aplicações, incluindo a impressão,
# a criação de documentos PDF e a produção gráfica em geral.
# o contrário das fontes bitmap, que são criadas a partir de pixels, 
# as fontes PostScript são criadas a partir de curvas e linhas vetoriais, 
# o que permite que sejam escaladas para qualquer tamanho sem perda
# de qualidade ou nitidez.

def font_demo(canvas, fonts):
    pos_y = 750
    for font in fonts:
        canvas.setFont(font, 12)
        canvas.drawString(30, pos_y, font)
        pos_y -= 10

canvas3 = canvas.Canvas("fonts.pdf", pagesize=letter)
fonts = canvas3.getAvailableFonts()
font_demo(canvas3, fonts)
canvas3.save()
