import os
from pypdf import PdfReader, PdfWriter

def fix_metadata(pdf_path):
    print(f"Traitement de {pdf_path}")
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Get existing metadata
        metadata = reader.metadata
        if metadata:
            new_metadata = {k: v for k, v in metadata.items()}
        else:
            new_metadata = {}

        # Modify Author and Title
        new_metadata.update({
            '/Author': 'Kevin ATES',
            '/Creator': 'Kevin ATES',
            '/Title': os.path.basename(pdf_path).replace('.pdf', ''),
            '/Producer': 'Kevin ATES'
        })

        writer.add_metadata(new_metadata)

        # Write to a temporary file, then replace original
        temp_path = pdf_path + ".tmp"
        with open(temp_path, "wb") as f:
            writer.write(f)
        
        os.replace(temp_path, pdf_path)
        print(f"Succès pour {pdf_path}")
    except Exception as e:
        print(f"Erreur pour {pdf_path}: {e}")

pdfs = [
    "COMPTE RENDU.pdf",
    "Compte Rendu - HD Pfsense .pdf",
    "Compte rendu - AD-GPO-SF.pdf",
    "KA Compte Rendu FSMO.pdf",
    "projet reseau.pdf",
    "projet systeme.pdf"
]

for pdf in pdfs:
    if os.path.exists(pdf):
        fix_metadata(pdf)
    else:
        print(f"Fichier introuvable: {pdf}")
