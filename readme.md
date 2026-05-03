# 🤖 Zac: Your Local Coding AI

**Zac** is a witty, local-first coding assistant powered by **Ollama** and the **Qwen3-Coder** model. Zac isn't just a chatbot; he has "hands"—meaning he can list, read, and write files directly within a secured workspace on your machine.

---

## 🚀 What Zac Does
- **Code Generation**: Writes full scripts and functions based on your prompts.
- **File Management**: Can create new files, read existing ones, and list directory contents.
- **Sandboxed Workspace**: Zac is restricted to a specific folder (`/zac_workspace`) to ensure he doesn't touch your system files.
- **Privacy**: Everything runs 100% locally on your hardware.

---

## 🛠️ Prerequisites

1.  **Python 3.10+** installed on your system.
2.  **Ollama** (The engine that runs the model).

---

## 📥 Installation Steps

### 1. Install & Setup Ollama
Download Ollama from [ollama.com](https://ollama.com) and install it for your OS.

Once installed, open your terminal and pull the model Zac uses:
```bash
ollama pull qwen3-coder
```
### 2. Create a Virtual Environment

Navigate to your project folder and set up a Python virtual environment to keep things clean.
Windows
```PowerShell

python -m venv venv
.\venv\Scripts\activate
```
macOS / Linux
```Bash

python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies

With your virtual environment active, install the required library:
```Bash
pip install ollama

```
###⚡ Running Zac

Ensure the Ollama application is running in your system tray.

Launch Zac by running:
```Bash

python zac.py
```
Zac will automatically create a folder called zac_workspace. This is the only place Zac can see or edit files.

#🎮 How to Talk to Zac

You can ask Zac to perform tasks across multiple files. For example:
```plaintext
    "Zac, check the workspace. If there is no 'app.py', create a basic Flask API."

    "Read 'logic.py' and tell me if there are any security vulnerabilities."

    "What files do I have in here right now?"

    "Update 'README.txt' to include today's date."
```
# 🛡️ Safety & Security

Zac is equipped with Path Validation. If he attempts to access a file outside of the ./zac_workspace directory (e.g., trying to read your SSH keys or system configs), the script will automatically block the request and return a permission error.
# 🐧 OS Compatibility

Step	Windows	macOS	Linux

Ollama, .exe Installer,	.zip / .dmg	Curl script

Python Command	python,	python3,	python3

Activate Venv	.\venv\Scripts\activate,	source venv/bin/activate,	source venv/bin/activate

