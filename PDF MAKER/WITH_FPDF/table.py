from fpdf import FPDF

pdf = FPDF()
pdf.set_font("Arial", size=12)
pdf.add_page()
    
col_width = pdf.w / 5
row_height = 15

def simple_table(spacing=1):
    data = [['S.NO','ITEM_TYPE','ITYPE_NAME','PRICE','PIC'],['1','TW','T-SHIRT','200',' '],['1','TW','T-SHIRT','200',' ']]          
    
    im_h = 26
    co = 0
    for row in data:
        co+=1
        for item in row:
            pdf.cell(col_width, row_height*spacing,txt=item, border=1)
        if co!=1:
            pdf.image('a.jpg', x=180, y=im_h, w=20)   
            im_h+=15     
        pdf.ln(row_height*spacing)
        
    pdf.output('simple_table.pdf')
    
if __name__ == '__main__':
    simple_table()