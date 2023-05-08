""" Page compression """

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from stylesheet import *
import time


start_time = time.time()

doc = SimpleDocTemplate(filename='aula04.pdf',
                        pagesize=A4,
                        rightMargin=72,
                        leftMargin=72,
                        topMargin=72,
                        bottomMargin=72,
                        pageCompression=True)

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ultrices nibh ac magna malesuada bibendum. Nunc laoreet, est non viverra pretium, orci ex placerat ex, ut blandit ex massa sed justo. Curabitur tempor turpis sit amet arcu efficitur imperdiet. Donec imperdiet, nisl quis tempor fringilla, nunc orci feugiat ante, vitae interdum nibh augue ac lacus. Cras quis turpis sagittis, pulvinar lorem ut, ultrices velit. Praesent rutrum sed quam eget auctor. Nam id dapibus dui. Morbi auctor augue eu porta feugiat. Maecenas tincidunt neque ac hendrerit efficitur. Suspendisse lacinia libero non tellus luctus convallis. Fusce et mattis orci, eget sollicitudin nulla'
flowables = [Paragraph(text, style=PARAGRAFO_NORMAL) for i in range(10000)]
doc.build(flowables)

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000

print(f"Tempo decorrido: {elapsed_time_ms:.2f} ms")
