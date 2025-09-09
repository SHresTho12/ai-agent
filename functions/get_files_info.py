

import os
from sys import deactivate_stack_trampoline
from google.genai import types

def get_files_info(working_directory, directory=None):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, directory)) if directory else base

    if os.path.commonpath([base,target]) != base:
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

    if os.path.commonpath([base,target]) != base:
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



def write_file(working_directory, file_path,content):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, file_path))

    if not (target == base or target.startswith(base + os.sep)):
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(target):
        try:
            with open(target, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Write fail to "{file_path}: {e}"'

    try:
        with open(target, "x") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Write fail to "{file_path}: {e}"'




## Schemas

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)




schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file contents of a specified file with a maximum of 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory from which file access is permitted",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file (relative to the working directory)",
            ),
        },
        required=["working_directory", "file_path"],
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file inside the working directory. Overwrites if file exists, otherwise creates a new one.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory from which file access is permitted",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file (relative to the working directory)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file",
            ),
        },
        required=["working_directory", "file_path", "content"],
    ),
)
