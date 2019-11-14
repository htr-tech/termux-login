import os
from getpass import getpass
import time
cread = '.creed.txt'

#--font colors---
red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1;93m'
blue = '\033[1;94m'
purple = '\033[1;95m'
cyan = '\033[1;96m'
white = '\033[1;97m'

def setup():
    if os.path.isfile(cread):
        login()
    else:
        singup()


def singup():
    try:
        clear()
        print(green + ' \t Welcome to Termux ')
        print(cyan + '---------------------------------')
        print(yellow + ' \t CREATED BY HTR TECH ')
        print('')
        os.system('date | lolcat')
        print("\033[1;93m")
        print(green + 'SET USERNAME,PASSWORD AND RECOVERY KEY')
        print('')
        username = str(input('\033[1;96mUsername \033[1;92m: '))
        password = input('\033[1;96mPassword \033[1;92m: ')
        print('')
        recovery = input(cyan + 'Enter a Recovery key \033[1;92m: ')
        print('')
        print(blue + "[+] Remember your recovery key.Without it you can't change username/pass")
        print('')
        x = input('\033[1;94mIf you agree hit Enter \033[1;94m: ')
        if x == '' or x:
            with open(cread, 'w') as (f):
                f.write(username)
                f.write('\n')
                f.write(password)
                f.write('\n')
                f.write(recovery)
                f.close()
                print('\n')
                print(blue + 'DONE ! Initializing ...')
                time.sleep(0.5)
                exit()
        else:
            print('\n')
            print(red + '     Wrong Input')
            time.sleep(0.4)
            singup()
    except Exception:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('\x1b[1;91m     UABLE TO SET THE USERNAME, PASSWORD, RECOVERY')
        time.sleep(0.3)
        os.system('killall -9 com.termux')
    except KeyboardInterrupt:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('\x1b[1;91m     UABLE TO SET THE USERNAME, PASSWORD, RECOVERY')
        time.sleep(0.3)
        os.system('killall -9 com.termux')


def singup_one():
    try:
        clear()
        print(green + ' \t Welcome to Termux ')
        print(cyan + '---------------------------------')
        print(yellow + ' \t CREATED BY HTR TECH ')
        print('')
        os.system('date | lolcat')
        print("\033[1;93m")
        print(green + 'SET USERNAME,PASSWORD AND RECOVERY KEY')
        print('')
        username = str(input(cyan + 'Username \033[1;92m: '))
        password = input(cyan + 'Password \033[1;92m: ')
        print('')
        recovery = input(cyan + 'Enter a Recovery key \033[1;92m: ')
        print('')
        print(blue + "[+] Remember your recovery key.Without it you can't change username/pass")
        print('')
        x = input('\033[1;94mIf you agree hit Enter \033[1;94m: ')
        if x == '' or x:
            with open(cread, 'w') as (f):
                f.write(username)
                f.write('\n')
                f.write(password)
                f.write('\n')
                f.write(recovery)
                f.close()
                print('\n')
                print(blue + 'DONE ! Initializing ...')
                time.sleep(0.5)
                exit()
        else:
            print('\n')
            print(red + '     Wrong Input')
            time.sleep(0.4)
            singup_one()
    except Exception:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('\x1b[1;91m     UABLE TO CHANGE THE USERNAME, PASSWORD, RECOVERY')
        time.sleep(0.4)
        os.system('killall -9 com.termux')
    except KeyboardInterrupt:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('\x1b[1;91m     UABLE TO CHANGE THE USERNAME, PASSWORD, RECOVERY')
        time.sleep(0.4)
        os.system('killall -9 com.termux')


def change():
    while True:
        clear()
        try:
            print(green + '[+] TO CHANGE THE PASSWORD PLEASE ENTER THE RECOVERY KEY')
            rec = getpass(cyan + ' \nEnter your Recovery \033[1;92m: ')
            with open(cread, 'r') as (fi):
                data = fi.readlines()
                reco = data[2].rstrip()
            if rec == reco:
                singup_one()
            else:
                print('\n')
                print(red + '    Invalid Recovery Key')
                time.sleep(0.4)
                continue
        except Exception:
            print('')
            print('')
            print('')
            print('')
            print('')
            print(red + '    Wrong Input')
            time.sleep(0.3)
        except KeyboardInterrupt:
            print('')
            print('')
            print('')
            print('')
            print('')
            print(red + '     Wrong Input')
            time.sleep(0.3)


def login():
    while True:
        clear()
        print(green + ' \t Termux Login Script ')
        print(cyan + '---------------------------------')
        print(yellow + ' \t CREATED BY HTR TECH ')
        print('')
        os.system('date | lolcat')
        print('')
        print(green + '[+] To change password type "change" in username or password')
        print('\x1b[1;93m ')
        with open(cread, 'r') as (fl):
            data = fl.readlines()
            uname = data[0].rstrip()
            pword = data[1].rstrip()
            fl.close()
        try:
            login = input(cyan + 'Username \033[1;92m: ')
            print('\n')
            login2 = getpass(cyan + 'Password \033[1;92: ')
            if login == uname:
                pass
            if login2 == pword:
                print('\n')
                print(yellow + '\n WELCOME ==> ', uname, '\x1b[0m')
                time.sleep(0.4)
                clear()
                break
            elif login == 'change' or login2 == 'change':
                change()
            else:
                print('\n')
                print(red + '     Wrong Input')
                time.sleep(0.4)
        except Exception:
            print('')
            print('')
            print('')
            print('')
            print('')
            print(red + '     Wrong Input')
            time.sleep(0.3)
        except KeyboardInterrupt:
            print('')
            print('')
            print('')
            print('')
            print('')
            print(red + '     Wrong Input')
            time.sleep(0.3)


def clear():
    os.system('clear')


def exit():
    os.system('killall -9 com.termux')


if __name__ == '__main__':
    setup()
