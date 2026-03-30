import pyautogui
import time

print('===================================')
print('  ')
print('O QUE VOCÊ QUER ASSISTIR?')
print('  ')
print('===================================')
print('  ')
midia = str(input())
print('  ')
print('===================================')

# Abre o navegador 
pause = 0.5
pyautogui.PAUSE = pause
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=809, y=464)

# Abre a HBO max
pyautogui.write('play.hbomax.com')
pyautogui.press('enter')

# Aguarda a página carregar e pesquisa a mídia desejada
time.sleep(10)
pyautogui.click(x=1694, y=152)
time.sleep(2)
pyautogui.write(midia)
pyautogui.press('enter')
time.sleep(2)

# Seleciona a mídia e inicia a reprodução
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('f11')