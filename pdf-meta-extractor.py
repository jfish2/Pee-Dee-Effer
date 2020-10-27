#pdf-meta-extractor.py

import pdfx
import json
import os


user_pdf = input("Please copy and paste the pdf here (ensure that the file to be analyzed is placed in the same folder as this python file!): \t")
pdf = pdfx.PDFx(str(user_pdf))
print('Analyzing PDF...')
meta = pdf.get_metadata()
url = pdf.get_references_as_dict()


with open('pdf-metadata.txt', 'w') as pdf_data:
  pdf_data.write('\nPDF Metadata \t')
  pdf_data.write(json.dumps(meta))
  pdf_data.write('\n')
  if len(url) == 0:
      pdf_data.close()
  else:
      for reference in url:
        pdf_data.write(reference)
  pdf_data.close()
