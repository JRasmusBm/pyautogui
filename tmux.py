import pyautogui
import sys
import time

_, routine = sys.argv


def tmux_hotkey():
    pyautogui.hotkey("ctrl", "s")


def new_window():
    tmux_hotkey()
    pyautogui.typewrite("c")


def pane_below():
    tmux_hotkey()
    pyautogui.typewrite('"')


def pane_right():
    tmux_hotkey()
    pyautogui.typewrite("%")


def switch_to_window(n):
    tmux_hotkey()
    pyautogui.typewrite(str(n))


def run(command):
    pyautogui.typewrite(command)
    pyautogui.hotkey("ctrl", "m")


def recipe_client():
    run("z recipe app")
    run("npm start")
    pane_right()
    run("z recipe app")
    run("npm run test:watch")
    new_window()
    run("z recipe app")
    run("vim")
    new_window()
    run("z recipe app")
    switch_to_window(2)


def recipe_server():
    run("z recipe server")
    run("docker rm -f $(docker ps -a -q)")
    run("docker-compose down; docker-compose -f docker-compose-dev.yml up")
    pane_right()
    run("sleep 5;")
    run("docker exec -ti recipe-server-dev-test sh")
    new_window()
    run("z recipe server")
    run("vim")
    new_window()
    run("z recipe server")
    switch_to_window(1)


def rise_server():
    run("z rise server")
    run("docker-compose -f docker-compose-dev.yml up")
    new_window()
    run("z rise server")
    run("vim")
    new_window()
    run("z rise server")
    switch_to_window(2)


def rise_client():
    run("z rise client")
    run("docker-compose -f docker-compose-dev.yml up")
    new_window()
    run("z rise client")
    run("vim")
    new_window()
    run("z rise client")
    switch_to_window(2)


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


if __name__ == "__main__":
    if routine == "recipe-server":
        recipe_server()
    if routine == "recipe-client":
        recipe_client()
    if routine == "rise-server":
        rise_server()
    if routine == "rise-client":
        rise_client()
    if routine == "taxi":
        taxi()
