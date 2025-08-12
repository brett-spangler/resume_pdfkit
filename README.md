# Brett Spangler Resume PDF Generator

This project generates a professional PDF resume from HTML templates using Python, Jinja2, and pdfkit (wkhtmltopdf). It supports dynamic content, custom footer rendering, and multiple resume versions.

## Features
- **HTML to PDF**: Converts Jinja2-rendered HTML resumes to PDF using `pdfkit` and `wkhtmltopdf`.
- **Dynamic Content**: Injects up-to-date links and last-updated dates into the resume.
- **Custom Footer**: Renders a styled footer with page numbers and version info.
- **Multiple Versions**: Easily switch between resume versions (e.g., automation, backend) via command-line.

## Requirements
- Python 3.7+
- [wkhtmltopdf](https://wkhtmltopdf.org/) (must be installed separately)
- Python packages: `pdfkit`, `jinja2`

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

### 1. Install wkhtmltopdf
- Download and install from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html).
- Note the path to the `wkhtmltopdf.exe` executable (e.g., `C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe`).

### 2. Generate a Resume PDF
Run from the project root:
```sh
python main.py --version automation --wkhtmltopdf "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
```
- `--version`: Resume version (e.g., `automation`).
- `--output`: (Optional) Output PDF path. Default: `output/Brett_Spangler_Resume.pdf`.
- `--wkhtmltopdf`: (Recommended) Path to your `wkhtmltopdf` executable.

### 3. Output
- The generated PDF will be saved to the `output/` directory.

## Project Structure
```
resume_pdfkit/
├── main.py                  # Main script: renders and generates PDF
├── generate_resume.py       # Standalone function for HTML-to-PDF
├── requirements.txt         # Python dependencies
├── output/                  # Generated PDFs
├── resume_versions/
│   ├── automation.html      # Resume HTML template (Jinja2)
│   └── footer_template.html # Footer HTML template (Jinja2)
└── ...
```

## Customization
- **Templates**: Edit or add HTML templates in `resume_versions/`.
- **Footer**: Update `footer_template.html` for custom footer content.
- **Context**: Modify the `context` dictionary in `main.py` for links, dates, etc.

## Debugging & Development
- VS Code launch config is provided in `.vscode/launch.json` for easy debugging.
- Temporary files (e.g., `rendered_footer.html`) are auto-removed after PDF generation.

## License
MIT License. See `LICENSE` file if present.