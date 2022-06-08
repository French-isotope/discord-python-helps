import os

path_dayz = "C:/Program Files (x86)/Steam/steamapps/common/DayZ/DayZ.exe"

def go_pew(answer):
    if answer:
        print('yeah lezgo')
        return True
    else:
        print('Ohno')
        return False

def ask_4_pew():
    pew = input('pew ?')
    try:
       go_pew(pew)
    except:
        print(f'Exception error (Bad Friend) : pew not working, change friend and try again')
        return False

    print('Launching DayZ')
    os.startfile(os.path(path_dayz))
    return True


if __name__ == "__main__":
    while(True):
        ask_4_pew()
