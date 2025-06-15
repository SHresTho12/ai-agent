

import os

def get_files_info(working_directory, directory=None):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, directory)) if directory else base

    if not (target == base or target.startswith(base + os.sep)):

        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if it's a valid directory
    if not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory'

    try:
        for t in os.listdir(target):
            t_path = os.path.join(target,t)
            if os.path.isfile(t_path):
                print(f"- {t}: file_size={os.path.getsize(t_path)} bytes, is_dir=False")
            else:
                print(f"- {t}: file_size={os.path.getsize(t_path)} bytes, is_dir=True")
    except:
        return f"Error: Cannot list contents of {directory}"
    

def get_file_content(working_directory, file_path):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, file_path))

    if not (target == base or target.startswith(base + os.sep)):
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'

    # Check if it's a valid file
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    try:
        with open(target, 'r', encoding='utf-8') as file:
            content = file.read()
            if len(content) > MAX_CHARS:
                truncated_msg = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                content = content[:MAX_CHARS] + truncated_msg
            return content
    except Exception as e:
        return f"Error: Cannot read file {file_path}: {str(e)}"