"""
This script extracts TEXT only from PDF. It will not do anything with images. Try to use the PDFSegmenter from JinaHub to see if that will allow you to work with both the images and text.
"""

#pip install pymupdf
from docarray import Document, DocumentArray
import fitz


pdf = fitz.open('data/somatosensory.pdf')
da = DocumentArray([Document(text=page.get_text()) for page in pdf])

def main() -> None:
    print(da[:,'text'])


if __name__ == '__main__':
    main()