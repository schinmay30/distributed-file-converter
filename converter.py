from fpdf import FPDF
import os

def convert_file(input_path, output_path):
    try:
        if input_path.endswith(".txt"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            with open(input_path, "r") as file:
                for line in file:
                    pdf.cell(200, 10, txt=line.strip(), ln=True)

            output_pdf = output_path.replace(".txt", ".pdf")
            pdf.output(output_pdf)

            return True

        else:
            # fallback (copy file)
            with open(input_path, "r") as f:
                data = f.read()
            with open(output_path, "w") as f:
                f.write(data)

            return True

    except Exception as e:
        print("Conversion error:", e)
        return False