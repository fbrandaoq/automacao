# importação da biblioteca usando um alias
import pyautogui as auto
import time

# define espera para cada comando auto
auto.PAUSE = 0.5

# abre o menu iniciar
auto.press('win')
# abre o chromechrome
auto.write('chrome')
auto.press('enter')

# maximizar a tela
auto.hotkey('alt','space')
auto.press('x')

# abre o github
auto.write('github.com')
# dar o enter
auto.press('enter')

# abre o classroom em uma nova guia
time.sleep(3) #atrasa a próxima ação separada, 3 segundos
auto.hotkey('ctrl','t')
auto.write('classroom.google.com')
auto.press('enter')

