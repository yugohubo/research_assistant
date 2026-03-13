from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import ScrapeWebsiteTool

from markdown_pdf import MarkdownPdf, Section

# 1. Scrape aracını standart şekilde başlatıyoruz
scrape_website_tool = ScrapeWebsiteTool()

# 2. DuckDuckGo aracını arka planda çalışması için başlatıyoruz
_ddg_backend = DuckDuckGoSearchRun()

# 3. LangChain aracını CrewAI'ın kabul edeceği bir formata sarıyoruz
@tool("DuckDuckGo Search Tool")
def ddg_search_tool(query: str) -> str:
    """
    It is used to search for current information, news, or any topic on the internet. 
    The agent only needs to provide the search query (as text) to this tool.
    """
    return _ddg_backend.run(query)

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


@tool("MarkdownToPDFTool")
def MarkdownToPDFTool(dummy_arg: str = "ignore") -> str:
    """
        This tool reads a typed Markdown (.md) file and saves it by converting it into a formatted "
        PDF (.pdf) file. You should use it for reporting and file output.
    """
    md_file_path = "report.md"
    pdf_file_path = "report.pdf"
    try:
        # Dosyanın var olup olmadığını kontrol et
        if not os.path.exists(md_file_path):
            return f"Error: A file named {md_file_path} could not be found. Please ensure the file has been created."

        # Markdown içeriğini oku
        with open(md_file_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        # PDF'e dönüştür ve kaydet
        pdf = MarkdownPdf()
        pdf.add_section(Section(md_content))
        pdf.save(pdf_file_path)

        return f"Successful: The file '{md_file_path}' has been successfully converted and saved as '{pdf_file_path}'."
            
    except Exception as e:
        return f"An error occurred during the conversion process: {str(e)}"