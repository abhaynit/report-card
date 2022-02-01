#https://pyfpdf.readthedocs.io/en/latest/reference/set_font/index.html
from fpdf import FPDF
 
# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
pdf=FPDF(format='letter', unit='in')
# Add new page. Without this you cannot create the document.
pdf.add_page()
# Set font face to Times, size 10.0 pt
pdf.set_font('Times','',10.0)
 
# Set color red
pdf.set_text_color(255,0,0)    
pdf.cell(1.0,0.0,'Hello World!')
# Line break 0.15 inches height
pdf.ln(0.15)
 
# Set color green
pdf.set_text_color(0,255,0)    
pdf.cell(1.0,0.0,'Hello World!')
pdf.ln(0.15)
 
# Set color blue
pdf.set_text_color(0,0,255)    
pdf.cell(1.0,0.0,'Hello World!')
pdf.ln(0.15)
 
# output content into a file ('F') named 'hello3.pdf'
pdf.output('hello3.pdf','F')