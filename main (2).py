<<<<<<< HEAD
from classes import Hboautomation

bot = Hboautomation(None, 0.5)
bot.executar()  
=======
from funções import abrir_navegador
from funções import abrir_hbomax
from funções import iniciar_reproducao
from funções import pesquisar_midia
from funções import perguntar_midia

midia = perguntar_midia()

abrir_navegador()

abrir_hbomax()

pesquisar_midia(midia)

iniciar_reproducao()
>>>>>>> 7fca44b44fcda2a4d4f3fe2e725fb5ae070df423
