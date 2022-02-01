from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.cell(200, 0, txt="Welcome to Python!", ln=1, align="C")



def pri():
    pdf.output("add_image.pdf")

def add_image(image_path,ab):
    pdf.image(image_path, x=ab, y=20, w=50)
    
    
    #pdf.set_font("Arial", size=12)
    #pdf.ln(85)  # move 85 down
    #pdf.cell(ab, bc, txt="{}".format(image_path), ln=1)
    
    
if __name__ == '__main__':
    add_image('a.jpg',0)
    add_image('a.jpg',100)
    pri()