import pyautogui as gui
from time import sleep
import pyperclip


gui.hotkey("winleft", "h", interval=0.05)  # Whatever command you use to switch windows

sleep(2)  # Time enough to hover the spot where the name appears in the channel info
heading_position = gui.position()

for i in range(500):
    sleep(0.2)
    gui.click(clicks=3, interval=0.1)
    sleep(0.2)
    gui.hotkey("ctrl", "c")
    channel_name = pyperclip.paste().strip()
    print(channel_name)
    sleep(0.2)
    gui.hotkey("esc")
    sleep(0.2)
    gui.hotkey("alt", "down")
    sleep(0.2)
    gui.hotkey("shift", "ctrl", "i")
