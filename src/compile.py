import subprocess
import os

def compile_latex(tex_path: str, output_dir: str) -> None:
    """
    Compiles a LaTeX file to PDF using pdflatex.

    Args:
        tex_path (str): Path to the .tex file.
        output_dir (str): Directory where the PDF will be saved.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Run pdflatex twice to resolve references
    for _ in range(2):
        result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                f"-output-directory={output_dir}",
                tex_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode != 0:
            print("LaTeX compilation error:")
            print(result.stdout.decode())
            print(result.stderr.decode())
            raise RuntimeError("Failed to compile LaTeX file.")

    print(f"✅ PDF generated in: {output_dir}")
