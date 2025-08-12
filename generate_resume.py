import pdfkit

def generate_resume(html_content: str, output_path: str = "output/Brett_Spangler_Resume.pdf", wkhtmltopdf_path: str = None):
    """
    Generates a PDF resume from HTML content.

    Args:
        html_content (str): The HTML string to convert.
        output_path (str): Path to save the generated PDF.
        wkhtmltopdf_path (str): Optional path to wkhtmltopdf executable.
    """
    config = None
    if wkhtmltopdf_path:
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    pdfkit.from_string(html_content, output_path, configuration=config)
    print(f"✅ Resume generated: {output_path}")