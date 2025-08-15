# src/generate.py
import google.generativeai as genai
from utils import read_file, write_file
import os
from dotenv import load_dotenv
import json

load_dotenv()  # Load .env file

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_resume(template_path, json_path, prompt_path, output_path):
    """
    Combines LaTeX template and JSON info using Gemini API
    and writes the filled LaTeX file to output_path.
    """
    # Read input files
    template_content = read_file(template_path)
    json_content = read_file(json_path)
    prompt_content = read_file(prompt_path)

    # Combine everything into one prompt for Gemini
    full_prompt = f"""
    {prompt_content}

    LaTeX Template:
    {template_content}

    Resume Data (JSON):
    {json_content}
    """

    # Create Gemini model instance
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Send prompt to Gemini
    response = model.generate_content(full_prompt)

    # Save LaTeX output
    write_file(output_path, response.text)

    print(f"LaTeX resume generated at {output_path}")
