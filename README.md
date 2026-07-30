# TermuxGPT

## AI-Powered Modular Android Automation Assistant

TermuxGPT is an open-source AI-powered automation assistant that connects Android applications with a Python execution engine.

The project is designed to transform natural language commands into real device actions through an intelligent command system, while keeping the architecture flexible through a powerful plugin system.

Instead of creating a fixed automation application, TermuxGPT provides a platform where new abilities can be added like game mods.

Users and developers can extend the assistant by creating new plugins without changing the core system.

---

# Main Features

## AI Command Understanding

TermuxGPT uses an AI engine to understand user requests and convert them into executable commands.

Examples:
Turn on flashlight

Send notification

Vibrate the phone 5 times

The system analyzes the request, creates a structured command, then sends it to the correct action handler.

---

# Android-Python Bridge

TermuxGPT uses a bridge architecture between Android and Python.

The Android application is responsible for:

- User interface
- Displaying commands
- Showing results
- Communicating with the backend


The Python engine is responsible for:

- AI processing
- Command routing
- Automation logic
- Plugin execution


Architecture:
Android Application | | Bridge Layer | | Python Automation Engine | | Plugin System | | Device Features

---

# Plugin System

TermuxGPT contains a modular plugin system.

Plugins work similar to game mods.

Each plugin can add new abilities:

Examples:

- Battery monitoring
- Flashlight control
- Vibration control
- Notifications
- Application management
- Custom automation


Plugin folder:
plugins/

Example:
plugins/ │ ├── battery.py ├── flashlight.py ├── vibrate.py └── my_plugin.py

---

# Creating Your Own Plugin

Create a new Python file inside:
plugins/

Example:

`plugins/example.py`

```python
ACTION = "example"

DESCRIPTION = "Example plugin"


def run(command):

    return {
        "success": True,
        "message": "Plugin executed"
    }
``Restart TermuxGPT.
The plugin loader will automatically detect the new plugin.
Secure API Key System
TermuxGPT does not store API keys inside the source code.
On the first startup:
The user is asked to enter the AI API key.
The input is hidden while typing.
The key is saved locally.
Future launches automatically load the saved key.
Configuration file:
user_config.json
Example:
{
    "API_KEY": "YOUR_API_KEY"
}
The configuration file should never be uploaded to GitHub.
Requirements
Android Application
Required:
Android 8 or newer
Termux (for Python backend)
Internet connection for AI requests
Development Requirements
Install:
Python 3.10+
Git
Gradle
Android SDK
Python packages:
pip install -r requirements.txt
Installation
1. Clone Repository
git clone https://github.com/yonukwasim520-cyber/TermuxGPT.git
Enter directory:
cd TermuxGPT
2. Install Python Backend
Install dependencies:
pip install -r requirements.txt
Start backend:
python app.py
3. Build Android Application
Go to Android project folder:
cd TermuxGPT-App
Build APK:
gradle :app:assembleDebug
The APK will be generated at:
app/build/outputs/apk/debug/
Install:
app-debug.apk
First Setup
When starting TermuxGPT for the first time:
Start the Python backend.
Open the Android application.
Enter your AI API key.
Wait for connection.
Start sending commands.
Example Automation
TermuxGPT supports event-based automation.
Examples:
When charging starts:
Send notification
When battery reaches 10%:
Vibrate five times
When a custom event happens:
Execute plugin
Project Structure
TermuxGPT

│
├── app.py
├── ai_router.py
├── automation.py
├── tools.py
│
├── plugins/
│   ├── battery.py
│   ├── flashlight.py
│   └── vibrate.py
│
├── TermuxGPT-App/
│   └── Android Application
│
└── config files
Development Philosophy
TermuxGPT is designed around three principles:
Modular
New features can be added through plugins.
Flexible
The system is not limited to predefined commands.
Expandable
The assistant can grow into a complete personal automation platform.
Future Features
Planned:
Voice commands
Visual plugin manager
Plugin marketplace
More Android integrations
Local AI model support
Advanced automation editor
Background service mode
License
Open-source project created for learning, development, and personal automation.
