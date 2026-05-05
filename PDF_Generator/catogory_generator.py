from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

OUTPUT = "sample_pdfs"
os.makedirs(OUTPUT, exist_ok=True)


# 🧾 Packing Slip PDF
def create_packing_slip(num):
    path = f"{OUTPUT}/Slip_{num}.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(100, 700, f"Packing Slip")
    c.drawString(100, 680, f"Slip No: {num}")
    c.save()


# 🚗 Mileage PDF
def create_mileage(plate):
    path = f"{OUTPUT}/Mileage_{plate}.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(100, 700, "Mileage Report")
    c.drawString(100, 680, f"Vehicle: {plate}")
    c.drawString(100, 660, "Mileage data...")
    c.save()


# 📊 Tachograph PDF
def create_tacho(plate, driver=None):
    name = f"Tacho_{plate}"
    if driver:
        name += f"_{driver}"

    path = f"{OUTPUT}/{name}.pdf"
    c = canvas.Canvas(path, pagesize=letter)

    c.drawString(100, 700, "Tachograph Report")
    c.drawString(100, 680, f"Vehicle: {plate}")

    if driver:
        c.drawString(100, 660, f"Driver: {driver}")

    c.save()


# 🔥 Generate sample PDFs
def generate_all():
    create_packing_slip(10492)
    create_packing_slip(10493)

    create_mileage("AB-123-C")
    create_mileage("XX-987-Y")

    create_tacho("AB-123-C")
    create_tacho("TR-UCK-01", "John Doe")
    create_tacho("TR-UCK-01", "Sarah Smith")
    create_tacho("TR-UCK-01", "Mike Johnson")


if __name__ == "__main__":
    generate_all()