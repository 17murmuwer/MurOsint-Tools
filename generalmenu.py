import os
import webbrowser

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def return_to_main():
    input("Нажмите Enter для возврата в главное меню...")
    main()

def byusername():
    clear_console()
    print("1. Userrecon")
    print("2. Sherlock")
    print("3. mailcat. Поиск email по никнейму")
    print("4. List of useful sites")
    print("5. unve1ler 100% нужный инструмент особенно по ru")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")

    if choice == "1":
        os.system("git clone https://github.com/issamelferkh/userrecon.git")
        os.chdir("userrecon")
        os.system("chmod +x userrecon.sh")
        os.system("bash userrecon.sh")
        return_to_main()

    elif choice == "2":
        if not os.path.exists("sherlock"):
            os.system("git clone https://github.com/sherlock-project/sherlock.git")
            os.chdir("sherlock")
        username = input("Введите имя пользователя: ")
        os.system(f"python3 sherlock {username}")
        return_to_main()

    elif choice == "3":
        if not os.path.exists("mailcat"):
            os.system("git clone https://github.com/sharsil/mailcat")
            os.chdir("mailcat")
            os.system("pip3 install aiohttp_socks")
            os.system("pip3 install requests_html")
        username = input("Введите имя пользователя: ")
        os.system(f"python3 mailcat.py {username}")
        return_to_main()

    elif choice == "4":
        webbrowser.open("https://www.idcrawl.com/")
        return_to_main()

    elif choice == "5":
        if not os.path.exists("unve1ler"):
            os.system("git clone https://github.com/spyboy-productions/unve1ler.git")
            os.chdir("unve1ler")
            os.system("pip3 install -r requirements.txt")
        os.system("python3 unve1ler.py")
        return_to_main()

    elif choice == "0":
        return_to_main()

    else:
        print("Неверный выбор")

def emailsearch():
    clear_console()
    print("1. Eyes. Сбор информации по email")
    print("2. EmailAll. Сбор информации по доменам.")
    print("3. Holele. Очень полезная штука!")
    print("4. Hunter.io. Поиск email адресов по домену.")
    print("5. Anymailfinder Site")
    print("6. Epios 100%  полезная штука")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")

    if choice == "1":
        if not os.path.exists("Eyes"):
            os.system("git clone https://github.com/N0rz3/Eyes.git")
            os.chdir("Eyes")
            os.system("pip3 install -r requirements.txt")
        email = input("Введите email: ")
        os.system(f"python3 eyes.py {email}")
        return_to_main()

    elif choice == "2":
        if not os.path.exists("EmailAll"):
            os.system("git clone https://github.com/Taonn/EmailAll.git")
            os.chdir("EmailAll")
            os.system("pip3 install -r requirements.txt")
        domain = input("Введите домен, например eljur.gospmr.org:  ")
        os.system(f"python3 emailall.py --domain {domain} run")
        return_to_main()

    elif choice == "3":
        if not os.path.exists("holehe"):
            os.system("git clone https://github.com/megadose/holehe.git")
            os.chdir("holehe")
            os.system("sudo python3 setup.py install")
        email = input("Введите email: ")
        os.system(f"holehe {email}")
        return_to_main()

    elif choice == "4":
        webbrowser.open("https://hunter.io/")
        return_to_main()

    elif choice == "5":
        webbrowser.open("https://newapp.anymailfinder.com/search/single")
        return_to_main()

    elif choice == "6":
        webbrowser.open("https://epieos.com")
        return_to_main()

    elif choice == "0":
        return_to_main()

    else:
        print("Неверный выбор")

def iptracker():
    clear_console()
    print("1. MurIptracker")
    print("2. Открыть сайты")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")

    if choice == "1":
        os.system("python iptracker.py")
        return_to_main()

    elif choice == "2":
        webbrowser.open("https://www.whois.com/whois")
        webbrowser.open("https://ipinfo.io/")
        webbrowser.open("https://www.ip2location.com/demo/")
        webbrowser.open("https://www.maxmind.com/en/geoip-web-services-demo")
        return_to_main()

    elif choice == "0":
        return_to_main()

    else:
        print("Неверный выбор")

def photosearch():
    clear_console()
    print("1. Открыть сайты")
    print("2. Хорошая коллекция Osint инструментов")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")

    if choice == "1":
        webbrowser.open("https://pimeyes.com/ru/results/nQd_240514r6p09xx0tduc35f6cad3d0a?query=ffefcfc3c3c2c0c08d1c1c1e3e3e3c3c&safesearch=true")
        webbrowser.open("https://search4faces.com/search.html")
        webbrowser.open("https://findclone.ru/")
        webbrowser.open("https://vk.watch/")
        webbrowser.open("https://photosherlock.com/")
        webbrowser.open("https://facecheck.id/")
        return_to_main()

    elif choice == "2":
        webbrowser.open("https://start.me/p/0PgzqO/photo-osint")
        return_to_main()

    elif choice == "0":
        return_to_main()

    else:
        print("Неверный выбор")

def telegramsearch():
    clear_console()
    print("1. telerecon")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")
    if choice == "1":
        if not os.path.exists("Telerecon"):
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("git clone https://github.com/sockysec/Telerecon.git")
            os.system("pip install -r requirements.txt")
            os.system("python3 -m spacy download en_core_web_sm")
            os.system("python3 setup.py")
        else:
            os.chdir("Telerecon")
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("pip install -r requirements.txt")
            os.system("python3 -m spacy download en_core_web_sm")
            os.system("python3 launcher.py")

def phone():
    clear_console()
    print("1. phomber")
    print("2. Mokuton На русском")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")
    if choice == "1":
        if not os.path.exists("phomber"):
            os.system("git clone https://github.com/s41r4j/phomber")
            os.chdir("phomber")
            os.system("pip3 install -r pyproject.toml")
            os.system("pip install phomber")
        os.system("python3 phomber.py")
        return_to_main()
    elif choice == "2":
        os.system("apt install git")
        os.system("pip install phonenumbers")
        os.system(f"python phone.py")

def bydiscord():
    clear_console()
    print("1. полезные сайты для поиска по id")
    choice = input("Выберите опцию (для выхода введите exit): ")
    if choice == "1":
        webbrowser.open("https://discord.id/")
        webbrowser.open("https://pfpfinder.com/tools/discord-lookup")
        webbrowser.open("https://discordlookup.com/user")
        return_to_main()
    elif choice.lower() == "exit":
        return_to_main()
    else:
        print("Неверный выбор")

def activedox():
    clear_console()
    print("1. Camphish - Ссылка создает сайт, можно получить фото жертвы, сайт можно сделать под себя.По умолчанию 3 сайта")
    print("2. Grabcam - Ссылка создает сайт, можно получить фото жертвы, сайт можно сделать под себя")
    print("3. Facad1ng - Маскировка фишинг ссылки")
    print("4. r4ven - Имба вещь. Через фишинг получает Photo/Ip/Локацию/Информацию об устройстве")
    choice = input("Выберите опцию (для возврата в главное меню введите 0): ")
    if choice == "1":
        if not os.path.exists("CamPhish"):
            os.system("apt-get -y install php openssh git wget")
            os.system("git clone https://github.com/techchipnet/CamPhish")
            os.chdir("CamPhish")
            os.system("bash camphish.sh")
    elif choice == "2":
        if not os.path.exists("grabcam"):
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("pkg install python -y")
            os.system("pkg install python2 -y")
            os.system("pkg install git -y")
            os.system("pip install lolcat")
            os.system("git clone https://github.com/noob-hackers/grabcam")
            os.chdir("$HOME/grabcam")
            os.system("bash grabcam.sh")
    elif choice == "3":
        if not os.path.exists("Facad1ng"):
            os.system("git clone https://github.com/spyboy-productions/Facad1ng.git")
            os.chdir("Facad1ng")
            os.system("pip3 install -r requirements.txt")
        os.system("python3 facad1ng.py")
    elif choice == "4":
        if not os.path.exists("r4ven"):
            os.system("git clone https://github.com/spyboy-productions/r4ven.git")
            os.chdir("r4ven")
            os.system("pip3 install -r requirements.txt")
        os.system("python3 r4ven.py")
    elif choice == "0":
        return_to_main()
    else:
        print("Неверный выбор")

def main():
    clear_console()
    print('''
    
• ▌ ▄ ·. ▄• ▄▌▄▄▄  • ▌ ▄ ·. ▄• ▄▌▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄      ▄▄▄▄▄            ▄▄▌  .▄▄ · 
·██ ▐███▪█▪██▌▀▄ █··██ ▐███▪█▪██▌██· █▌▐█▀▄.▀·▀▄ █·    •██  ▪     ▪     ██•  ▐█ ▀. 
▐█ ▌▐▌▐█·█▌▐█▌▐▀▀▄ ▐█ ▌▐▌▐█·█▌▐█▌██▪▐█▐▐▌▐▀▀▪▄▐▀▀▄      ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
██ ██▌▐█▌▐█▄█▌▐█•█▌██ ██▌▐█▌▐█▄█▌▐█▌██▐█▌▐█▄▄▌▐█•█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪ ▀▀▀ .▀  ▀     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 
                                                                                   
''')                                                                                 
                                                                                   
                                                                                   
                                                                                 
    print("Главное меню")
    print("1. Имя пользователя")
    print("2. Ip-Адрес")
    print("3. По номеру телефона")
    print("4. Поиск по фото")
    print("5. Email")
    print("6. Telegram")
    print("7. Discord")
    print("8. Instagram")
    print("9. ActiveDox")
    choice = input("Выберите опцию (для выхода введите exit): ")

    if choice == "1":
        byusername()
    elif choice == "2":
        iptracker()
    elif choice == "3":
        phone()
    elif choice == "4":
        photosearch()
    elif choice == "5":
        emailsearch()
    elif choice == "6":
        telegramsearch()
    elif choice == "7":
        bydiscord()
    elif choice == "8":
        # Ваш код для поиска по Instagram
        pass
    elif choice == "9":
        activedox()
    elif choice.lower() == "exit":
        exit()
    else:
        print("Неверный выбор")

    return_to_main()

if __name__ == "__main__":
    main()
