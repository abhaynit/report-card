from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

image_path1 = 'front.jpeg'
image_path2 = 'back.jpeg'
pdf.image(image_path1, x=10, y=20, w=80)
pdf.image(image_path2, x=120, y=20, w=80)
pdf.output("add_image.pdf")