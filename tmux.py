import pyautogui
import sys
import time

_, routine = sys.argv


def new_window():
    pyautogui.hotkey("ctrl", "s")
    pyautogui.typewrite("c")


def pane_below():
    pyautogui.hotkey("ctrl", "s")
    pyautogui.typewrite('"')


def pane_right():
    pyautogui.hotkey("ctrl", "s")
    pyautogui.typewrite("%")


def switch_to_window(n):
    pyautogui.hotkey("ctrl", "s")
    pyautogui.typewrite(str(n))


def run(command):
    pyautogui.typewrite(command)
    pyautogui.hotkey("ctrl", "m")


def recipe_client():
    run("z rec a")
    run("npm start")
    pane_right()
    run("z rec a")
    run("npm run test:watch")
    new_window()
    run("z rec a")
    run("vim")
    new_window()
    run("z rec a")
    switch_to_window(2)

def recipe_server():
    run("z rec s")
    run("docker rm -f $(docker ps -a -q)")
    run("docker-compose down; docker-compose -f docker-compose-dev.yml up")
    pane_right()
    run("sleep 5;")
    run("docker exec -ti recipe-server-dev-test sh")
    new_window()
    run("z rec s")
    run("vim")
    new_window()
    run("z rec s")
    switch_to_window(1)


def taxi():
    for _ in range(4):
        run("z tax")
        new_window()
    run("z mongodb")
    run("docker rm -f $(docker ps -a -q)")
    run("docker-compose down; docker-compose up")
    switch_to_window(2)
    run("vim")
    switch_to_window(4)
    run("z tax re")
    run("vim")
    switch_to_window(3)
    pane_below()
    run("z tax re")
    switch_to_window(1)
    run("grunt")
    pane_below()
    run("z tax re")
    run("grunt")
    switch_to_window(2)


def haskell():
    run("z dec")
    new_window()
    run("z dec")
    run("vim")
    run(":Ex")
    pane_right()
    run("z dec")
    run("stack ghci")
    new_window()
    run("z dec")
    switch_to_window(2)


if routine == "recipe-server":
    recipe_server()
if routine == "recipe-client":
    recipe_client()
if routine == "taxi":
    taxi()
if routine == "haskell":
    haskell()
