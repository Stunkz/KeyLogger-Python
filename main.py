import keyboard

def main():
    while True:
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            break