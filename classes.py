import pyautogui
import time

class Hboautomation:
    def __init__(self, pausa):
        self.midia = None
        self.pausa = pausa

    def esperar(self, x):
        time.sleep(x)

    def botao_perfil(self):
        pyautogui.click(x=809, y=464)

    def botao_pesquisa(self):
        pyautogui.click(x=1694, y=152)

    def tela_cheia(self):
        pyautogui.press('f11')

    def abrir_navegador(self):
        pyautogui.PAUSE = self.pausa
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        self.esperar(4)
        self.botao_perfil()

    def abrir_hbomax(self):
        pyautogui.write('play.hbomax.com')
        pyautogui.press('enter')

    def pesquisar_midia(self, midia):
        self.esperar(10)
        self.botao_pesquisa()
        self.esperar(5)
        pyautogui.write(midia)
        pyautogui.press('enter')
        self.esperar(2)
    
    def iniciar_reproducao(self):
        self.esperar(2)
        pyautogui.press('down')
        pyautogui.press('enter')
        self.esperar(3)
        pyautogui.press('tab')
        pyautogui.press('enter')
        self.esperar(1)
        self.tela_cheia()

    def perguntar_midia(self):
        print('----------------------------')
        print('O que você deseja assistir? ')
        print('----------------------------')
        midia = str(input())
        print('----------------------------')
        return midia
    
    def executar(self):
        self.midia = self.perguntar_midia()
        self.abrir_navegador()
        self.abrir_hbomax()
        self.pesquisar_midia(self.midia)
        self.iniciar_reproducao()