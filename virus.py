import time
import pyautogui


alturaTela, larguraTela = pyautogui.size()

print(alturaTela, larguraTela)

eixoX, eixoY = pyautogui.position()

print(eixoX, eixoY)

pyautogui.move(488, 735)

pyautogui.click(488, 735)

time.sleep(2)

pyautogui.write("cmd")

time.sleep(2)

pyautogui.press("enter")

time.sleep(5)

pyautogui.write(r'echo "Pedro Benjamin, Antonio Artur, Carlos Augusto, Ana Cecilia, Isaac Nilson" > C:\Users\pedbe\OneDrive\Documentos\\arquivo.txt')

time.sleep(3)

pyautogui.press("enter")

time.sleep(2)

pyautogui.write("exit")

pyautogui.press("enter")