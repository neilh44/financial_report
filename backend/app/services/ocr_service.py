from docling import OCRProcessor  # Example with Docling

def extract_text_from_pdf(pdf_path: str) -> dict:
    processor = OCRProcessor(language="auto")
    result = processor.process_file(pdf_path)
    return result
