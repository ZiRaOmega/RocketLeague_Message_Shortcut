# Rocket League Shortcut Manager

This Python script provides a simple graphical user interface (GUI) for managing keyboard shortcuts that send predefined chat messages in Rocket League when the game window is active.

## Features

- **Add Shortcut**: Create new keyboard shortcuts to send specific messages in Rocket League.
- **Delete Shortcut**: Remove existing shortcuts.
- **Persistent Storage**: Shortcuts are stored in a JSON file and loaded each time the script runs.
- **Active Window Check**: The script only sends messages when Rocket League is the active window.

## Installation

Before running the script, ensure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install pyautogui keyboard pygetwindow tkinter
```
Usage
1. Starting the Script: Run the script with Python.
```bash
python rocket_league_shortcut_manager.py
```
2. Adding a Shortcut:
Click the "Add Shortcut" button.
Enter the desired keyboard shortcut (e.g., ctrl+shift+d).
Enter the message you want to send in Rocket League.
The shortcut is now active and will function when Rocket League is the active window.
3. Deleting a Shortcut:
Select the shortcut you want to delete from the list.
Click the "Delete Shortcut" button to remove it.

4. Using a Shortcut:
While playing Rocket League, use the defined keyboard shortcuts to send the associated messages.

### File Structure
rocket_league_shortcut_manager.py: The main Python script.
shortcuts.json: A JSON file where the shortcuts are stored.

## Notes
The script must be running in the background for the shortcuts to work.
Shortcuts are global and may conflict with other system or application shortcuts.
The script requires administrative privileges to detect key presses on some systems.
## License
This script is for personal use and is not affiliated with or endorsed by Rocket League or its affiliates.