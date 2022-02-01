# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
	[ "ITEMS","PRICE"],
	
] 


pdf = SimpleDocTemplate( "receipt1.pdf" , pagesize = A4 )
styles = getSampleStyleSheet()
title_style = styles[ "Heading1" ]
title_style.alignment = 1
title = Paragraph( "BILL GENERATOR" , title_style )
style = TableStyle()
table = Table( DATA , style = style )
pdf.build([ title , table ])
