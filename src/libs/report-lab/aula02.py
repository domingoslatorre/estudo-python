""" Aula 02 - Page Layout """

# PLATYPUS - Page Layout and Typography Using Scripts

# DocTemplates - the outermost container of your page
# PageTemplates - specifies the layout of your page
# Frames - kind of like a sizer in a desktop user interface. Basically it provides a region that contains other flowables
# Flowables - A text or graphic element that can be “flowed” across page boundaries, such as a paragraph of text. This does not
# include footers and headers. 

# pdfgen.Canvas - The lowest level of ReportLab, and one that we have already covered. It will actually receive its instructions
# from one or more of the upper layers and “paint” your document accordingl

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

doc = SimpleDocTemplate(filename='hello_doc.pdf',
                        pagesize = A4, 
                        rightMargin = 72, 
                        leftMargin = 72, 
                        topMargin = 72, 
                        bottomMargin = 72)

# Mostrar a implementação da função
# Mostrar que devolve um instância de
# uma classe que se comporta como dict
stylesheet = getSampleStyleSheet()

# Cria uma lista de objetos flowables (fluídos) - fluir pelas páginas
flowables = []

# Instancia um paragrafo é define a formataçao
header_01 = Paragraph('Título do documento', style=stylesheet['Heading1'])
# Adiciona o paragrafo na lista de flowables
flowables.append(header_01)

paragraph_text_01 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ultrices nibh ac magna malesuada bibendum. Nunc laoreet, est non viverra pretium, orci ex placerat ex, ut blandit ex massa sed justo. Curabitur tempor turpis sit amet arcu efficitur imperdiet. Donec imperdiet, nisl quis tempor fringilla, nunc orci feugiat ante, vitae interdum nibh augue ac lacus. Cras quis turpis sagittis, pulvinar lorem ut, ultrices velit. Praesent rutrum sed quam eget auctor. Nam id dapibus dui. Morbi auctor augue eu porta feugiat. Maecenas tincidunt neque ac hendrerit efficitur. Suspendisse lacinia libero non tellus luctus convallis. Fusce et mattis orci, eget sollicitudin nulla'
paragraph_01 = Paragraph(paragraph_text_01, style=stylesheet['BodyText'])
flowables.append(paragraph_01)

paragraph_text_02 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ultrices nibh ac magna malesuada bibendum. Nunc laoreet, est non viverra pretium, orci ex placerat ex, ut blandit ex massa sed justo. Curabitur tempor turpis sit amet arcu efficitur imperdiet. Donec imperdiet, nisl quis tempor fringilla, nunc orci feugiat ante, vitae interdum nibh augue ac lacus. Cras quis turpis sagittis, pulvinar lorem ut, ultrices velit. Praesent rutrum sed quam eget auctor. Nam id dapibus dui. Morbi auctor augue eu porta feugiat. Maecenas tincidunt neque ac hendrerit efficitur. Suspendisse lacinia libero non tellus luctus convallis. Fusce et mattis orci, eget sollicitudin nulla'
paragraph_02 = Paragraph(paragraph_text_02, style=stylesheet['BodyText'])
flowables.append(paragraph_02)

header_02 = Paragraph('Título 2 do documento', style=stylesheet['Heading2'])
flowables.append(header_02)

for i in range(30):
    flowables.append(Paragraph(paragraph_text_01, style=stylesheet['BodyText']))

# Construi o documento usando uma lista de flowables
doc.build(flowables)





