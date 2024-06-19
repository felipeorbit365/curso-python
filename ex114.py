# Mudei para YouTube porque o site do Pudim estava dando erro por poder ser malicioso
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site do YouTube não está acessível no momento.')
else: 
    print('Consegui acessar o site do YouTube com sucesso!')
