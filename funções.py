import pyautogui
import time

def abrir_navegador():
    pausa = 0.5
    pyautogui.PAUSE = pausa
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=809, y=464)

def abrir_hbomax():
    pyautogui.write('play.hbomax.com')
    pyautogui.press('enter')

def pesquisar_midia(midia):
        # Aguarda a página carregar e pesquisa a mídia desejada
        time.sleep(10)
        pyautogui.click(x=1694, y=152)
        time.sleep(5)
        pyautogui.write(midia)
        pyautogui.press('enter')
        time.sleep(2)
    
def iniciar_reproducao():
        # Seleciona a mídia e inicia a reprodução
        time.sleep(2)
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('f11')

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