from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.set_font("helvetica", size=10)
pdf.cell(200, 10, txt="Whi abhay!", ln=2, align="C")
pdf.output("simple_demo.pdf")

