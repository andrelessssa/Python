

import pyautogui
import time

pyautogui.keyDown("command")
time.sleep(0.1)  # Aguarde 100ms
pyautogui.press("space")
pyautogui.keyUp("command")
pyautogui.write("chrome")
pyautogui.press("enter")