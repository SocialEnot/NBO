import socket
from Banners import BannerNBOStart, BannerNBOStop
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
init()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
#Все настройки NBO
passnboserv = '13112008'

client_color = random.choice(colors)
Vibor = input("Использовать IP адрес по умолчанию?(Y/N) ")
if Vibor == 'Y':
    Password = input("Введите пороль установленный на сервер 'NBO' - ")
    if Password == passnboserv:
        SERVER_HOST = "109.191.204.168"
        SERVER_PORT = 9090
    else:
        print("Error 0x1 - Не корректный пороль от сервера")
        print("Пороль не верен! Вы перенаправлены на локальное подключение")
        SERVER_HOST = "localhost"
        SERVER_PORT = 9090
else:
    SERVER_HOST = input("Введите ip адрес сервера - ")
    SERVER_PORT = input("Введите порт подключения к серверу(до 65535) - ")

separator_token = "<SEP>" 
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
print(BannerNBOStart)
name = input("Enter your name: ")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)
t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send =  input()
    if to_send.lower() == 'q':
        print("Вы отключены от сервера")
        break
    if to_send.lower() == 'admin':
        print("@Mynamels")
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())
s.close()
print(Fore.RED, BannerNBOStop)
