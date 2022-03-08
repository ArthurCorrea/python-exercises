# Crie um código em Python que teste se o site
# Pudim está acessível pelo computador usado.
import webbrowser
try:
    webbrowser.open_new('pudim.com.br')
    print('Site acessível.')
except:
    print('Site inacessível no momento!')

# Resolução do professor
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site inacessível.')
else:
    print('Site acessível.')
    print(site.read())
