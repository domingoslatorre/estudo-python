from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import *

TITULO_01 = ParagraphStyle(
    name='Titulo1',
    fontSize=20,
    spaceAfter=50,
    alignment=TA_CENTER,
)

PARAGRAFO_NORMAL = ParagraphStyle(
    name='ParagrafoNormal',
    fontSize=12,
    spaceAfter=12,
    leading=16,
    alignment=TA_JUSTIFY,
    firstLineIndent=30,
)

PARAGRAFO_NORMAL_PRIMEIRO = ParagraphStyle(
    name='ParagrafoNormalPrimeiro',
    parent=PARAGRAFO_NORMAL,
    firstLineIndent=0,
)


PARAGRAFO_DETALHE = ParagraphStyle(
    name='ParagrafoDetalhe',
    fontSize=10,
    spaceBefore=25,
    spaceAfter=25,
    leading=12,
    alignment=TA_JUSTIFY,
    leftIndent=130,
    rightIndent=0,
)
