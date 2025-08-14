# src/utils.py
def read_file(path):
    """Read and return the content of a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    """Write text content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
