try:
    import os
    import colorama
    from colorama import Fore
    from colorama import Style
    import pyfiglet
    from pyfiglet import Figlet
except:
    import os
    os.system('pip3 install pyfiglet')
    os.system('pip3 install colorama')
    exit('[+] Setup Success, Please Command to start tool : python3 main.py')
yellow = f"{Fore.YELLOW}{Style.BRIGHT}"
red = f"{Fore.RED}{Style.BRIGHT}"
green = f"{Fore.GREEN}{Style.BRIGHT}"
reset = f"{Style.RESET_ALL}"
colorama.init()

def scripting():
    os.system('cls' if os.name == 'nt' else 'clear')
    fs = Figlet(font='slant')
    print(fs.renderText('Dora Hacking'))
    print(f"""
Telegram : {green}@Chrome2024{reset}
Donate {yellow}BTC{reset} :  [ {green}17L22i227Keet23QCNaeCyrQ6xfiTQpQJ5{reset} ]
Note: the above tool may cause damage to infrastructure
Please use it for the best possible purpose
""")
