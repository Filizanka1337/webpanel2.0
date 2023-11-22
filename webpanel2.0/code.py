# Importowanie
import os
import time
import threading

# Instalacja Flask
os.system("pip install Flask")

from flask import Flask, render_template  # Import render_template

# Instalacja modułu colorama
os.system("pip install colorama")

from colorama import init, Fore

# Inicjalizacja colorama
init(autoreset=True)

# Definiowanie
app = Flask(__name__)

def start_ssh():
    os.system("systemctl enable ssh")
    print(Fore.YELLOW + "SSH enabled")
    os.system("systemctl start ssh")
    print(Fore.YELLOW + "SSH server started")

def access_ssh_www():
    threading.Thread(target=os.system, args=("wssh",)).start()
    print(Fore.YELLOW + "WSSH started on port 8888")

def install_dependencies():
    os.system("apt update")
    print(Fore.GREEN + "Updated packages ")
    os.system("apt install openssh-server -y")
    print(Fore.GREEN + "Installed SSH server")
    os.system("pip install webssh")
    print(Fore.YELLOW + "WebSSH installed")

def show_commands():
    print("Available commands:")
    print("- start_ssh")
    print("- access_ssh_www")
    print("- install_dependencies")
    print("- list")
    print("- help")
    print("- exit")

# Tekst na czerwono
red_text = Fore.RED + " ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄        ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄ \n"\
                     "█ █ ▄ █ █       █  ▄    █  █       █      █  █  █ █       █   █      █       █    █  ▄    █\n"\
                     "█ ██ ██ █    ▄▄▄█ █▄█   █  █    ▄  █  ▄   █   █▄█ █    ▄▄▄█   █      █▄▄▄▄   █    █ █ █   █\n"\
                     "█       █   █▄▄▄█       █  █   █▄█ █ █▄█  █       █   █▄▄▄█   █       ▄▄▄▄█  █    █ █ █   █\n"\
                     "█       █    ▄▄▄█  ▄   █   █    ▄▄▄█      █  ▄    █    ▄▄▄█   █▄▄▄   █ ▄▄▄▄▄▄█▄▄▄ █ █▄█   █\n"\
                     "█   ▄   █   █▄▄▄█ █▄█   █  █   █   █  ▄   █ █ █   █   █▄▄▄█       █  █ █▄▄▄▄▄█   ██       █\n"\
                     "█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄▄█   █▄█ █▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄▄▄██▄▄▄▄▄▄▄█"

# Wyświetlenie tekstu na czerwono
print(red_text)

# Napis w kolorze Fore.LIGHTBLUE_EX
blue_text = Fore.LIGHTBLUE_EX + " __________________\n"\
                               "|  ______________  |\n"\
                               "| | run as root    | |\n"\
                               "| | help, list     | |\n"\
                               "| |______________| |\n"\
                               "|__________________|"

# Wyświetlenie napisu w niebieskim kolorze
print(blue_text)

# Funkcja uruchamiająca aplikację Flask
def run_flask_app():
    app.run(host='0.0.0.0', port=5678)

# Wątek dla aplikacji Flask
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.start()

# Dynamiczne dodanie route dla index.html
@app.route('/')
def index():
    with open('index.html', 'r') as file:
        html_content = file.read()
    return html_content

# Czekanie na input od użytkownika
while True:
    user_input = input("Wprowadź komendę (wpisz 'help' dla pomocy): ").strip().lower()

    if user_input == 'exit':
        break
    elif user_input == 'start_ssh':
        start_ssh()
    elif user_input == 'access_ssh_www':
        access_ssh_www()
    elif user_input == 'install_dependencies':
        install_dependencies()
    elif user_input == 'list':
        show_commands()
    elif user_input == 'help':
        print("Komendy:")
        print("- start_ssh: Uruchamia SSH server.")
        print("- access_ssh_www: Uruchamia WSSH na porcie 8888.")
        print("- install_dependencies: Instaluje niezbędne zależności.")
        print("- list: Wyświetla dostępne komendy.")
        print("- help: Wyświetla pomoc.")
        print("- exit: Kończy program.")
    else:
        print("Nieprawidłowa komenda. Wpisz 'list' aby zobaczyć dostępne komendy.")
