# Rotate pages of a PDF file using PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileWriter


def rotate_pages(pdf_path):
    """Rotate pages of a PDF file.
    Reminder: PdfFileReader rotating methods only accept multiples of 90 as angles.
    """
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)

    # Rotate page 90 degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)

    # Rotate page 90 degrees to the left
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)

    # Rotate page upside down
    page_3 = pdf_reader.getPage(2).rotateCounterClockwise(180)
    pdf_writer.addPage(page_3)

    # Add a page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(3))

    with open('data/rotate_pages.pdf', 'wb') as fh:
        #  Make sure that the title of your file doesn't match an existing document, or it'll overwrite it!
        # fh = file handler
        # 'wb' = 'write' and 'binary' modes of opening a file
        pdf_writer.write(fh)


if __name__ == '__main__':
    path = 'data/Jupyter_Notebook.pdf'
    rotate_pages(path)
