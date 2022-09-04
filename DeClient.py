B = '\u0040\u006C\u0061\u006D\u0065\u0072\u0031\u0031\u0032\u0033\u0031\u0031' #blue
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

import urllib.request
import webbrowser
import random
from datetime import datetime
import getpass
import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp
from shutil import which
from colorama import init 
from colorama import Fore, Back, Style
import smtplib
import multiprocessing
from os import system
import re
version = '1.5'
time.sleep(3)
os.system('termimage Decl.jpg')
print(G + '[+]' + C + ' Проверка обновлений.....', end='')
ver_url = 'https://raw.githubusercontent.com/pashokkok/DeClient/main/version.txt'
try:
	ver_rqst = requests.get(ver_url)
	ver_sc = ver_rqst.status_code
	if ver_sc == 200:
		github_ver = ver_rqst.text
		github_ver = github_ver.strip()

		if version == github_ver:
			print(C + '[' + G + ' Актуально ' + C +']' + '\n')
		else:
			print(C + '[' + G + ' Доступно : {} '.format(github_ver) + C + ']' + '\n')
			print(R + '[-] Пожалуйста, обновите DeClient до актуальной версии \n')
			newver = input(G + '[1]' + C + 'Как мне обновить DeClient до новой версии? \n' + G + '[2]' + C + 'Выйти' + G + '\nMe4Sploit ==> ')
			if newver == "1" :
				print(Fore.MAGENTA)
				print('Пункт 1: Зайдите в наш телеграм канал: dark_softcode')
				time.sleep(3)
				print('Пункт 2: Напишите Админу @ImOmnipotent для получения новой версии')
				time.sleep(3)
				print('Удачи! Мы вас ждем с новой версией!')
				time.sleep(5)
				exit()
			if newver == "2":
				exit()
			
	else:
		print(C + '[' + R + ' Статус : {} '.format(ver_sc) + C + ']' + '\n')
except Exception as e:
	print('\n' + R + '[-]' + C + ' Исключение : ' + W + str(e))

def choice():
	print(C)
	print('█▀▄ █▀▀ █▀▀ █░░ █ █▀▀ █▄░█ ▀█▀')
	print('█▄▀ ██▄ █▄▄ █▄▄ █ ██▄ █░▀█ ░█░')
	print("DeClient@" + getpass.getuser() + "          |  Support  |        ")
	print("DeClient@" + getpass.getuser() + "   Termux |   Linux   | Windows")
	print("DeClient@" + getpass.getuser() + "          |    1.5    |        ")
	print("DeClient@" + getpass.getuser() + "          |  DeClient |        ")
	print("DeClient@" + getpass.getuser() + "          |     BY    |        ")
	print("DeClient@" + getpass.getuser() + "          |IOmnipotent|        ")
	print(G + '[1]' + C + ' Tools')
	print(G + '[2]' + C + ' DeBomber')
	print(G + '[3]' + C + ' DeChec-[IP]')
	print(G + '[4]' + C + ' DeChec-[NUM]')
	print(G + '[5]' + C + ' DeBrute-[TANK]')
	print(G + '[6]' + C + ' Exit')
	print('\n')
	print(Fore.GREEN)
	option = input('DeClient ==>  ')
	if option == "1":
		print( Fore.GREEN )
		print('Tools')
		time.sleep(2)
		lists = input ('[Exit] Exit \n[1] Gemail-hack \n[2] B0mb3r \n[3] Mail-Spammer \n[4] Brute_Force \n[5] Grab-Cam \n[6] Shark \n[7] CrossFire Ddos \n[8] FaceBook_Brute \n[9] AresBomb \n[10] Track-Em \n[11] Cardesc \n[12] Insanity-Framework \n[13] Entropy Toolkit \n[14] Airgeddon \n[15] ISniff-GPS \n[16] Trape \n[17] Kali Nethunter \n[18] XAttacker \n[19] WordSteal \n[20] SpiderFoot \n[21] Instashell \n[22] VkFisher \n[23] Entropy \nDeClient ==>  ')
		
		if lists == "Exit":
			exit()
			
		if lists == "exit":
			exit()
			
		if lists == "1":
			os.system('git clone https://github.com/Ha3MrX/Gemail-Hack')
			
		if lists == "2":
			os.system('git clone https://github.com/Denishnc/b0mb3r')
			
		if lists == "3":
			os.system('git clone https://github.com/pashokkok/Mail_Smmp')
		
		if lists == "4":
			os.system('git clone https://github.com/Tim55667757/pwd_brut')
			
		if lists == "5":
			os.system('git clone https://github.com/noob-hackers/grabcam')
		
		if lists == "6":
			os.system('git clone https://github.com/Bhaviktutorials/shark')
			
		if lists == "7":
			os.system('git clone https://github.com/crossfireTeam/crossfireMSDOS')
			os.system('cd crossfireMSDOS')
			os.system('cmake CMakeLists.txt')
			os.system('chmod +x Makefile')
			
		if lists == "8":
			os.system('git clone https://github.com/pashokkok/FB')
			
		if lists == "9":
			os.system("pkg install git")
			os.system("pkg install python")
			os.system("pip install requests")
			os.system("git clone https://github.com/MaksPV/AresBomb")
			
		if lists == "10":
			os.system("git clone https://github.com/LiNuX-Mallu/Track-Em.git")
			
		if lists == "11":
			os.system("git clone https://github.com/escdroid/cardesc.git")
			
		if lists == "12":
			os.system("git clone https://github.com/4w4k3/Insanity-Framework")
		
		if lists == "13":
			os.system("pip install tailer")
			os.system("git clone https://github.com/evildevill/entropy")
			
		if lists == "14":
			os.system("git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
			
		if lists == "15":
			os.system("git clone https://github.com/hubert3/iSniff-GPS.git")
		
		if lists == "16":
			os.system("git clone https://github.com/jofpin/trape.git")
			
		if lists == "17":
			os.system("pkg install wget")
			os.system("termux-setup-storage")
			os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
			os.system("chmod 777 install-nethunter-termux")
			os.system("./install-nethunter-termux")
			
		if lists == "18":
			os.system("git clone https://github.com/Moham3dRiahi/XAttacker.git")
			
		if lists == "19":
			os.system("git clone https://github.com/0x09AL/WordSteal.git")
			
		if lists == "20":
			os.system("git clone https://github.com/smicallef/spiderfoot")
			
		if lists == "21":
			os.system("git clone https://github.com/tiptoettt/instashell")
			
		if lists == "22":
			os.system("git clone https://github.com/foxlitegor/fisher")
			
		if lists == "23":
			os.system("git clone https://github.com/evildevill/entropy")
			
		if lists == "24":
			os.system("git clone https://github.com/sc1341/TikTok-OSINT")

		else:
			print('ERROR: 102' + Fore.YELLOW + '$' + Fore.RED + 'Invalid Tool')
		
	if option == "2":
		print("Started")
		os.system("python bombdll.py -n")

	if option == "3" :
		print("Started")
		os.system("python ipdll.py")
		
	if option == "4":
		print("Started")
		numph = input("Номер телефона: +")
		os.system("python numdll.py -n" + numph)

	if option == "5":
		print("Started")
		os.system("python gmaildll.pyc")

	if option == "6" :
		exit()
		
try:
	choice()
	
except:
	print("end")

