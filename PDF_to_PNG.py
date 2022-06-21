from pdf2image import convert_from_path
pages = convert_from_path('pdf_file.pdf', 500)
for page in pages:
    page.save('out.png', 'PNG')