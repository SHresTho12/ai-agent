# ai-agent

## 📌 Overview

This project is an **AI-powered coding assistant** built on top of Google’s Gemini API.  
The assistant is designed to operate in a **restricted working directory** (currently set to `calculator/`).  
Within this sandboxed environment, it can:

- List files and directories
- Read file contents
- Create or edit files
- Execute Python files

This makes it useful for interactive coding tasks, debugging, and project management while ensuring **safe, controlled access** to the filesystem.

---

## 📂 Project Structure

```
├── calculator/ # Current working directory (sandbox)
│ ├── lorem.txt
│ ├── main.py
│ ├── pkg/
│ │ ├── calculator.py
│ │ ├── morelorem.txt
│ │ ├── render.py
│ │ └── pycache/ # Auto-generated cache files
│ ├── README.md
│ └── tests.py
│
├── functions/ # Contains tool definitions and executors
│ ├── function_executor.py
│ ├── get_files_info.py
│ ├── run_python.py
│ └── pycache/ # Auto-generated cache files
│
├── schemas/ # Function schemas for LLM tools
│
├── main.py # Entry point for running the assistant
├── requirements.txt # Python dependencies
├── README.md # Project documentation (this file)
└── tests.py # Top-level tests
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone <your-repo-url>
uv venv ai-agent ## I have used uv you can use any other tool to create virtual environment
cd ai-agent

source venv/bin/activate
```

2. Install Dependencies

```bash
uv pip install -r requirements.txt
```

Make sure you have Python 3.9+.

3. Environment Variables

Create a .env file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

## 🚀 Usage

Run Assistant

```bash
python main.py "your prompt here"
```

Example:

```bash
python main.py "List all files in the project"

```

### Verbose Mode

Enable detailed logging:

```bash
python main.py "Read main.py" --verbose
```

### 🔒 Restricted Workspace

The assistant is restricted to the calculator/ folder by default.
You can change the working directory to another safe location if required.

This ensures the LLM only operates within a controlled environment and cannot access system files outside the sandbox.

## Features

🗂 File exploration (list, read, create, edit)

🐍 Execute Python scripts with arguments

🔁 Iterative conversation until completion

🛡️ Safe restricted workspace

## 📌 Notes

This project is an early prototype (v1.0) and may evolve with new tools.
The assistant is not a general-purpose shell — it is limited to the functions explicitly defined in the functions/ module.
