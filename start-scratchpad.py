from pathlib import Path

import pyperclip
import pyautogui

previous_selection = pyperclip.paste()

pyautogui.hotkey("ctrl", "a", interval=0.20)
pyautogui.hotkey("ctrl", "c")

current_selection = pyperclip.paste()

if current_selection != previous_selection:
    file_name = Path("~/.scratchpad").expanduser()
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(current_selection.strip())
