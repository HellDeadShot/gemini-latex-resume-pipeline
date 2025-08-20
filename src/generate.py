import google.generativeai as genai
from src.utils import read_file, write_file
import os
from dotenv import load_dotenv
import json

load_dotenv()  # Load .env file

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_resume(template_path, json_data, prompt_path, output_path):
    """
    Combines LaTeX template and JSON info using Gemini API
    and writes the filled LaTeX file to output_path.
    """
    try:
        # Read input files
        template_content = read_file(template_path)
        prompt_content = read_file(prompt_path)
        json_content = json.loads(json_data)

        # Updated prompt to request only raw LaTeX without code fences
        full_prompt = f"""{prompt_content}

        IMPORTANT: Output ONLY the raw LaTeX code without any markdown code fences or backticks.

        LaTeX Template:
        {template_content}

        Resume Data (JSON):
        {json_content}
        """

        # Create Gemini model instance
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Send prompt to Gemini
        response = model.generate_content(full_prompt)

        # Clean output in case the model still adds code fences
        lines = response.text.splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        cleaned_output = "\n".join(lines)

        # Save LaTeX output
        write_file(output_path, cleaned_output)
        print(f"LaTeX resume generated at {output_path}")
    except Exception as e:
        print(f"Error generating resume: {e}")
