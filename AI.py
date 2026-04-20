import ollama
import os

# --- CONFIGURATION ---
# Define the only directory Zac is allowed to touch
WORKSPACE_DIR = os.path.abspath("./zac_workspace")

# Create the directory if it doesn't exist
if not os.path.exists(WORKSPACE_DIR):
    os.makedirs(WORKSPACE_DIR)

# --- UTILITIES ---

def safe_path(path):
    """Ensures the path is within the WORKSPACE_DIR to prevent path traversal."""
    full_path = os.path.abspath(os.path.join(WORKSPACE_DIR, path))
    if not full_path.startswith(WORKSPACE_DIR):
        raise PermissionError("Zac tried to leave the workspace! Access denied.")
    return full_path

# --- TOOLS FOR ZAC ---

def list_files(directory="."):
    """Lists all files and folders in Zac's workspace."""
    try:
        target = safe_path(directory)
        items = os.listdir(target)
        return f"Files in {directory}: " + ", ".join(items)
    except Exception as e:
        return f"Error listing files: {e}"

def read_file(path):
    """Reads the content of a file within the workspace."""
    try:
        target = safe_path(path)
        with open(target, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(path, content):
    """Writes content to a file within the workspace."""
    try:
        target = safe_path(path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file: {e}"

# Tool mapping
tools_map = {
    'list_files': list_files,
    'read_file': read_file,
    'write_file': write_file
}

# --- ZAC'S CORE LOGIC ---

def zac_chat(user_prompt):
    model_name = 'qwen3-coder-next'
    
    system_message = {
        'role': 'system', 
        'content': f"You are Zac, a coding AI. You are restricted to the workspace: {WORKSPACE_DIR}. "
                   "Always list files if you aren't sure what's available. "
                   "Be helpful, efficient, and maintain a professional but witty tone."
    }

    messages = [system_message, {'role': 'user', 'content': user_prompt}]

    # 1. Ask Zac what to do
    response = ollama.chat(
        model=model_name,
        messages=messages,
        tools=[list_files, read_file, write_file],
    )

    # 2. Handle tool calls (recursive loop to handle multiple steps)
    while response.message.tool_calls:
        messages.append(response.message)
        
        for tool in response.message.tool_calls:
            function_name = tool.function.name
            args = tool.function.arguments
            
            print(f"🔧 Zac action: {function_name}({args})")
            
            try:
                result = tools_map[function_name](**args)
            except PermissionError as e:
                result = str(e)
            
            messages.append({'role': 'tool', 'content': result, 'name': function_name})

        # Get Zac's thoughts after seeing the tool results
        response = ollama.chat(model=model_name, messages=messages)

    return response.message.content

# --- INTERACTIVE LOOP ---

if __name__ == "__main__":
    print(f"--- Zac is online. Workspace: {WORKSPACE_DIR} ---")
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']: break
        
        reply = zac_chat(query)
        print(f"\nZac: {reply}\n")
