import os
from langchain.tools import Tool

def generate_filename(code: str) -> str:
    # Extract the first few words or a specific identifier from the code
    lines = code.splitlines()
    function_name = "generated_code"  # Default name if no function is found

    for line in lines:
        if line.strip().startswith("def "):
            # Get the function name without the "def " prefix
            function_name = line.split("(")[0][4:].strip()
            break

    # Clean the function name to create a valid filename
    function_name = function_name.replace(" ", "_").replace("(", "").replace(")", "")
    
    # Avoid using special names like __init__ or __str__
    if function_name in ["__init__", "__str__", "__repr__"]:
        function_name = "custom_function"

    return f"{function_name}_code.py"

def save_to_txt(data: str):
    filename = generate_filename(data)  # Generate a unique filename based on the code
    try:
        formatted_text = f"\n\n{data}\n"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(formatted_text)

        print(f"Code successfully saved to {filename}")
        return f"Code successfully saved to {filename}"
    except Exception as e:
        print(f"Error writing to file: {e}")
        return f"Error writing to file: {e}"

save_tool = Tool(
    name="save_code_to_file",
    func=save_to_txt,
    description="Saves generated code to a Python file with a meaningful name.",
)