# Advanced Educational Keylogger

Created by: Hamza Kayyali

This is an advanced keylogger application created for educational purposes to understand input monitoring, background processes, and logging techniques. This project uses Python's pynput library to monitor keyboard inputs silently.

## Disclaimer
**Important:** This tool is for educational purposes only. Using keyloggers without explicit consent may be illegal. Only use this on your own devices or with explicit permission.

## Features
- Silent background operation
- Detailed keystroke logging with timestamps
- Handles special keys and key combinations
- Clean and organized log format
- Process detachment from terminal
- Graceful termination with Ctrl+K
- Minimal system resource usage
- No visible terminal output while running

## Requirements
- Python 3.x
- pynput library
- datetime module
- Linux/Unix-based system (for background process forking)

## Installation
1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the keylogger:
```bash
python keylogger.py
```

2. The keylogger will:
   - Start running silently in the background
   - Create a `keylog.txt` file in the same directory
   - Show a single startup message and detach from terminal
   - Continue logging until stopped

3. Stop the keylogger:
   - Press `Ctrl + K` to stop logging
   - The process will terminate cleanly

## Log File Format
The keylog.txt file will contain entries in the following format:
```
=== Keylogger Started at YYYY-MM-DD HH:MM:SS ===
YYYY-MM-DD HH:MM:SS: a
YYYY-MM-DD HH:MM:SS: b
YYYY-MM-DD HH:MM:SS: [ENTER]
YYYY-MM-DD HH:MM:SS: c
```

## Special Keys
The following special keys are logged with descriptive tags:
- [ENTER]
- [TAB]
- [SPACE]
- [SHIFT]
- [BACKSPACE]
- [CTRL]
- [ALT]
- [CAPS_LOCK]

## Security Notes
- The log file is stored in plain text
- No encryption is implemented by default
- The process runs with user permissions
- Can be detected by process monitoring tools

## Limitations
- Requires root/sudo for some key combinations on Linux
- May not capture all system-level key combinations
- Log file is not encrypted
- Only works on the local machine

## Future Improvements
- Log file encryption
- Remote logging capabilities
- System startup integration
- Mouse movement tracking
- Window focus tracking

## Note
This is an educational tool designed to demonstrate system monitoring concepts. Always respect privacy and obtain necessary permissions before deployment.

## Author
**Hamza Kayyali**
- Educational Project
- Created for learning purposes