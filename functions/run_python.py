import os
import subprocess
from google.genai import types

def run_python_file(working_directory,file_path,args=[]):

    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, file_path)) 

    if os.path.commonpath([base , target]) != base:
       return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target):
       return f'Error: File "{file_path}" not found.'
    if not target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
                ["python",target]+ args,
                cwd=base,
                capture_output=True,
                text=True,
                timeout=30,
                check=False)
        output_parts = []

        if completed_process.stdout:
            output_parts.append(f"STDOUT:\n{completed_process.stdout.strip()}")
        if completed_process.stderr:
            output_parts.append(f"STDERR:\n{completed_process.stderr.strip()}")

        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")

        if not output_parts:  # no stdout, no stderr
            return "No output produced."

        return "\n\n".join(output_parts)
    except Exception as e:
        return f'Error: An exception occurred while executing "{file_path}": {e}'





## Schema for the funciton


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file inside the permitted working directory with optional command-line arguments. Captures stdout, stderr, and exit code.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory from which the Python file should be executed",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file (relative to the working directory)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list of command-line arguments to pass to the Python file (default: empty list)",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["working_directory", "file_path"],
    ),
)
