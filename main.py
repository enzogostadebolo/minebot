from time import sleep
import pyautogui


def close_the_menu(back_to_game_path="images/backtogame.png"):
    pos = pyautogui.locateCenterOnScreen(back_to_game_path, confidence=0.7)
    pyautogui.moveTo(pos)
    pyautogui.click()


def break_a_block():
    pyautogui.mouseDown()
    # change the sleep time if you feel it necessary (iron pickaxe without enchantments by default)
    sleep(0.9)
    pyautogui.mouseUp()


def move_mouse_to(down=True):
    pos = 40 if down else -40
    pyautogui.moveRel(0, pos, 0.4)
    sleep(0.01)


def move_char():
    pyautogui.keyDown("w")
    sleep(0.1)
    pyautogui.keyUp("w")


def locate_lava(lava_path="images/lava.png"):
    # change the confidence if you still have problems with lava
    if pyautogui.locateCenterOnScreen(lava_path, confidence=0.4):
        pyautogui.keyDown("s")
        sleep(4)
        pyautogui.keyUp("s")
        return True


if __name__ == "__main__":
    sleep(3)
    close_the_menu()

    while not locate_lava():
        break_a_block()
        move_mouse_to(down=True)
        break_a_block()
        move_mouse_to(down=False)
        move_char()
