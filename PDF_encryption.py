# Ecript a PDF file using PyPDF

from PyPDF2 import PdfFileReader, PdfFileWriter

def add_encryption(input_pdf, output_pdf, password):
    """Encrypt a PDF file."""
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password,
                       owner_pwd=None,
                       use_128bit=True)
    
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    add_encryption(input_pdf='data/reportlab-sample.pdf',
                   output_pdf='data/reportlab-encrypted.pdf',
                   password='guest')
