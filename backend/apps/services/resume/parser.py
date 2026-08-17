
from pypdf import PdfReader
from docx import Document


def extract_text(file_path: str) -> str:
    """
    Extract text from PDF or DOCX file.
    """

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    elif file_path.endswith(".docx"):
        doc = Document(file_path)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        raise ValueError("Unsupported file format")