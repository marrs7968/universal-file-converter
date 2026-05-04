from fpdf import FPDF
from pathlib import Path

class Converter:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.converters = {
            ('.txt', '.pdf'): self.txt_to_pdf,
            ('.csv', '.xlsx'): self.csv_to_xlsx,
            ('.jpg', '.png'): self.jpg_to_png,
            # Add more converters as needed
        }

    def convert(self):
        input_path = Path(self.input_file)
        output_path = Path(self.output_file)

        input_ext = input_path.suffix
        output_ext = output_path.suffix

        if (input_ext, output_ext) in self.converters:
            self.converters[(input_ext, output_ext)]()
        else:
            print("Conversion not supported for the given file types.")
        
    def txt_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(self.input_file, 'r') as file:
            for line in file:
                pdf.multi_cell(0, 10, line.rstrip())

        pdf.output(self.output_file)
        print(f"Converted {self.input_file} to {self.output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Universal File Converter')
    parser.add_argument('input_file', type=str, help='The input file to convert')
    parser.add_argument('output_file', type=str, help='The output file after conversion')
    args = parser.parse_args()

    converter = Converter(args.input_file, args.output_file)
    converter.convert()