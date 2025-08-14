# src/main.py
import os
from dotenv import load_dotenv
from generate import generate_resume
from compile import compile_latex

# Load environment variables from .env
load_dotenv()

# Paths to files (adjust these if your files are in a different location)
TEMPLATE_PATH = "/home/helldeadshot/vs code/Latex/gemini-latex-resume-pipeline/data/template.tex"   # Path to your LaTeX template
JSON_PATH = "/home/helldeadshot/vs code/Latex/gemini-latex-resume-pipeline/data/sample_resume.json"          # Path to your resume data
PROMPT_PATH = "/home/helldeadshot/vs code/Latex/gemini-latex-resume-pipeline/data/gemini_prompt.txt" 
OUTPUT_TEX_PATH = "/home/helldeadshot/vs code/Latex/gemini-latex-resume-pipeline/output/resume.tex"
OUTPUT_PDF_PATH = "/home/helldeadshot/vs code/Latex/gemini-latex-resume-pipeline/output/resume.pdf"

def main():
    # Step 1: Generate LaTeX resume from Gemini API
    generate_resume(
        template_path=TEMPLATE_PATH,
        json_path=JSON_PATH,
        prompt_path=PROMPT_PATH,
        output_path=OUTPUT_TEX_PATH
    )

    # Step 2: Compile LaTeX to PDF
    compile_latex(OUTPUT_TEX_PATH, OUTPUT_PDF_PATH)

if __name__ == "__main__":
    main()
