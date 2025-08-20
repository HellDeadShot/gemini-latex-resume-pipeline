# src/main.py
import os
from dotenv import load_dotenv
from src.generate import generate_resume
from src.compile import compile_latex

# Load environment variables from .env
load_dotenv()

# Get the project root directory (parent of src)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to files relative to project root
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "data", "template.tex")
JSON_PATH = os.path.join(PROJECT_ROOT, "data", "sample_resume.json")
PROMPT_PATH = os.path.join(PROJECT_ROOT, "data", "gemini_prompt.txt")
OUTPUT_TEX_PATH = os.path.join(PROJECT_ROOT, "output", "resume.tex")
OUTPUT_PDF_PATH = os.path.join(PROJECT_ROOT, "output", "resume")

def resume_wrapper(data: dict):
    generate_resume(
        template_path=TEMPLATE_PATH,
        json_data=data,
        prompt_path=PROMPT_PATH,
        output_path=OUTPUT_TEX_PATH
    )

    # Step 2: Compile LaTeX to PDF
    compile_latex(OUTPUT_TEX_PATH, OUTPUT_PDF_PATH)