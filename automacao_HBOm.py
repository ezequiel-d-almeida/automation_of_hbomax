# Tentativa de melhorar minhas praticas de modularização de código e uso de funções.

import pyautogui
import time

def perguntar_midia():
    print('===================================')
    print('  ')
    print('O QUE VOCÊ QUER ASSISTIR?')
    print('  ')
    print('===================================')
    print('  ')
    midia = str(input())
    print('  ')
    print('===================================')
    return midia

def abrir_navegador():
    pause = 0.5
    pyautogui.PAUSE = pause
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=809, y=464)

def abrir_hbomax():
    pyautogui.write('play.hbomax.com')
    pyautogui.press('enter')

def iniciar_reproducao(midia):
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


midia = perguntar_midia()

# Abre o navegador 
abrir_navegador()

# Abre a HBO max
abrir_hbomax()

# Aguarda a página carregar e pesquisa a mídia desejada
# Seleciona a mídia e inicia a reprodução
iniciar_reproducao(midia)
