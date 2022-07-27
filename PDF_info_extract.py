# How to extract metadata from your PDF file with PyPDF2

# Import class from PyPDF2
from unicodedata import name
from PyPDF2 import PdfFileReader


def extract_information(pdf_path):
    """Extract metadata from a PDF file."""
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    
    txt = f"""
    Information about {pdf_path}:
    
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of Pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path = 'data/reportlab-sample.pdf'
    extract_information(path)