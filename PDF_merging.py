#  Merge PDF files with PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdfs(paths, output):
    """Merge PDF files by adding each page of the documents to a merged file 
    after iterating over the range of pages.
     """
    pdf_writer=  PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range (pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF file
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = ['data/document1.pdf', 'data/document2.pdf']
    merge_pdfs(paths, output='data/merged.pdf')