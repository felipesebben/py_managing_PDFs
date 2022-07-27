# Watermark a PDF file with PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

def create_watermark(input_pdf, output, watermark):
    """Watermark all pages of a PDF file."""
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages of a PDF file
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    create_watermark(
        input_pdf='data/reportlab-sample.pdf',
        output='data/watermarked_notebook.pdf',
        watermark='data/watermark.pdf'
    )