from pathlib import Path

import pyautogui
import pyperclip

file_name = Path("~/.scratchpad").expanduser()
with open(file_name, encoding="utf-8") as f:
    contents = f.read().strip()

print(contents)

pyautogui.hotkey("winleft", "h", interval=0.05)
pyautogui.hotkey("ctrl", "a", interval=0.05)
pyperclip.copy(contents)
pyautogui.hotkey("ctrl", "v", interval=0.05)
