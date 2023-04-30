import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Há erro')
else:
    print('Tudo certo')
    print(site.head())