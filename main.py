import os
import argparse
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit

def render_template(template_name: str, context: dict) -> str:
    folder = "resume_versions"
    env = Environment(loader=FileSystemLoader(folder))
    template = env.get_template(template_name)
    return template.render(context)

def save_rendered_footer(html: str, output_path: str = "rendered_footer.html"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    parser = argparse.ArgumentParser(description="Generate Brett Spangler's resume as a PDF.")
    parser.add_argument("--version", type=str, default="automation", help="Resume version: automation, backend, default")
    parser.add_argument("--output", type=str, default="output/Brett_Spangler_Resume.pdf", help="Output PDF path")
    parser.add_argument("--wkhtmltopdf", type=str, help="Path to wkhtmltopdf executable")
    parser.add_argument("--email", type=str, required=True, help="Email address to include in resume")
    parser.add_argument("--phone", type=str, required=True, help="Phone number to include in resume")

    args = parser.parse_args()


    # Dynamic context
    context = {
        "linkedin": "https://www.linkedin.com/in/brett-spangler-05498a13a",
        "github": "https://github.com/brett-spangler",
        "email": args.email,
        "phone": args.phone,
        "last_updated": datetime.today().strftime("%B %d, %Y"),
        "resume_version": args.version
    }

    # Render resume and footer
    resume_html = render_template(f"{args.version}.html", context)
    footer_html = render_template("footer_template.html", context)
    save_rendered_footer(footer_html)

    # PDF options
    options = {
        'footer-html': 'rendered_footer.html',
        'margin-top': '25mm',
        'margin-bottom': '20mm'
    }

    config = pdfkit.configuration(wkhtmltopdf=args.wkhtmltopdf) if args.wkhtmltopdf else None
    pdfkit.from_string(resume_html, args.output, options=options, configuration=config)
    os.remove('rendered_footer.html')

    print(f"✅ Resume generated: {args.output}")

if __name__ == "__main__":
    main()