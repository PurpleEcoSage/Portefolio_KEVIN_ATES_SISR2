import os
import pikepdf

def fix_metadata_pikepdf(pdf_path):
    print(f"Traitement de {pdf_path}")
    try:
        pdf = pikepdf.Pdf.open(pdf_path)

        # Clear existing XMP metadata to avoid conflicting info
        if "/Metadata" in pdf.Root:
            del pdf.Root.Metadata

        # Update document info dictionary
        with pdf.open_metadata() as meta:
            meta["dc:creator"] = ["Kevin ATES"]
            meta["dc:title"] = os.path.basename(pdf_path).replace(".pdf", "")
            meta["pdf:Author"] = "Kevin ATES"
            meta["pdf:Producer"] = "Kevin ATES"
            meta["xmp:CreatorTool"] = "Kevin ATES"

        # Overwrite standard PDF info just in case
        pdf.docinfo["/Title"] = os.path.basename(pdf_path).replace(".pdf", "")
        pdf.docinfo["/Author"] = "Kevin ATES"
        pdf.docinfo["/Creator"] = "Kevin ATES"
        pdf.docinfo["/Producer"] = "Kevin ATES"

        temp_path = pdf_path + ".tmp"
        pdf.save(temp_path)
        pdf.close()
        
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
        fix_metadata_pikepdf(pdf)
    else:
        print(f"Fichier introuvable: {pdf}")
