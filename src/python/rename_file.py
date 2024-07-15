import os

def rename_pdf_file(pdf_path, new_name):
    directory = os.path.dirname(pdf_path)
    new_path = os.path.join(directory, new_name + ".pdf")
    os.rename(pdf_path, new_path)
