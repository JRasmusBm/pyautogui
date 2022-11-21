import pyautogui as gui
from time import sleep

conversations = [
    "Doktor-se/book-svc",
    "Doktor-se/conversation-svc",
    "Doktor-se/prescription-svc",
    "Doktor-se/stats-svc",
    "Doktor-se/websocket-svc",
    "Doktor-se/care-bot",
]
genesis = [
    "Doktor-se/pay-svc",
    "Doktor-se/push-svc",
    "Doktor-se/user-svc",
    "Doktor-se/platform-config",
]
general = [
    "Doktor-se/app-api",
    "Doktor-se/postman_collections",
    "Doktor-se/schemas",
]
features = " ".join(["issues", "pulls", "commits", "releases", "reviews", "comments",])

gui.hotkey("winleft", "h", interval=0.05) # Whatever command you use to switch windows

for name in genesis + conversations:
    sleep(0.2)
    gui.write("/")
    sleep(0.2)
    gui.write("github ")
    # sleep(0.2)
    # gui.write(f"subscribe {name} {features}")
    sleep(0.2)
    gui.write(f"unsubscribe {name}")
    sleep(0.5)
    gui.hotkey("enter")

