![Logo](logo.png)






# TermuxGPT

## AI-Powered Modular Android Automation Assistant

TermuxGPT is an open-source AI automation assistant that combines an Android application with a Python-powered backend engine.

The project allows users to control device features, create automations, and interact with artificial intelligence using simple natural language commands.

The main idea behind TermuxGPT is to create an expandable assistant platform where new features can be added through plugins, similar to installing mods in games.

---

# Features

## AI Command System

TermuxGPT understands normal user requests and converts them into executable commands.

Examples:

```
Turn on flashlight
```

```
Send notification
```

```
Vibrate the phone
```

The AI analyzes the request and sends it to the correct action module.

---

# Project Architecture

TermuxGPT is divided into multiple parts:

```
Android Application
        |
        |
    Bridge System
        |
        |
 Python Automation Engine
        |
        |
   Plugin Manager
        |
        |
 Device Actions
```

## Android Application

The Android app provides:

- User interface
- Command input
- Results display
- Communication with the backend

## Python Engine

The Python system handles:

- AI communication
- Command processing
- Automation
- Plugin execution

---

# Plugin System

TermuxGPT uses a modular plugin architecture.

Plugins allow users to add new features without changing the main program.

Example plugin folder:

```
plugins/
│
├── battery.py
├── flashlight.py
├── vibrate.py
└── custom_plugin.py
```

Each plugin provides:

- Action name
- Description
- Execution function

---

# Creating a Plugin

Create a new file inside:

```
plugins/
```

Example:

File:

```
plugins/example.py
```

Code:

```
ACTION = "example"

DESCRIPTION = "Example plugin"


def run(command):

    return {
        "success": True,
        "message": "Plugin executed"
    }
```

Restart TermuxGPT.

The plugin manager will automatically detect the new plugin.

---

# API Key Setup

TermuxGPT uses a secure first-time setup system.

- Upon running the tool, the first thing it will ask you to type API Key 
- But a word of advice: don't share this key with anyone.
- Just write the API Key It will be saved API Key automatic
- Simply running another tool also doesn't require writing anything API Key Manual operation is no longer required as  the  process has been automated
---

# Requirements

## Android Requirements

- Android device
- Android 8 or newer
- Termux
- Internet connection


## Development Requirements

Required tools:

- Python 3.10+
- Git
- Gradle
- Android SDK


Python packages:

```
pip install -r requirements.txt
```

---

# Installation

## Download Source Code

Clone the repository:

```
git clone https://github.com/yonukwasim520-cyber/TermuxGPT.git
```

Open the folder:

```
cd TermuxGPT
```

---

# Running Python Backend

Install dependencies:

```
pip install -r requirements.txt
```

Start the backend:

```
python app.py
```

The backend will start listening for commands from the Android application.

---

# Building Android Application
Download our app

---

# First Usage

After installation:

1. Start the Python backend.
2. Open the Android application.
3. Connect the application with the backend.
4. Enter your AI API key.
5. Start sending commands.

Example:

```
Send notification
```

```
Turn on flashlight
```

```
Vibrate five times
```

---

# Automation System

TermuxGPT supports event-based automation.

Examples:

```
When charging starts:
Send notification
```

```
When battery reaches 10%:
Vibrate five times
```

```
When a custom event happens:
Run plugin action
```

---

# Folder Structure

```
TermuxGPT/

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
└── TermuxGPT-App/
    └── Android Project
```

---

# Security

TermuxGPT follows a safer design:

- API keys are not included in source code.
- Private configuration files are ignored.
- User settings stay locally stored.
- Plugin system separates features from the core engine.

---

# Future Plans

Planned features:

- Voice commands
- Visual plugin manager
- More Android integrations
- Plugin marketplace
- Advanced automation editor
- Local AI model support

---

# License

Open-source project for learning, development, and personal automation.
