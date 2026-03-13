from markdown_pdf import MarkdownPdf, Section
import os
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "report.md")

with open(file_path, "r", encoding="utf-8") as f:
    md_content = f.read()


# Read the markdown content from a file
# with open("report.md", "r", encoding="utf-8") as f:
#     md_content = f.read()

# Create a MarkdownPdf object
pdf = MarkdownPdf()

# Add a section with your markdown content
pdf.add_section(Section(md_content))

# Save the pdf document to a file
pdf.save("report.pdf")