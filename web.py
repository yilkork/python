from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

# Veri cekilecek adres
url = "https://www.investing.com/currencies/gau-try"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)

# web sayfasina baglan ve sayfanin html kodlarini page degiskenine al
try:
    page = urlopen(req)
except:
    print("Error opening the URL")

# html kodlarini BeautifulSoup ile parse et ve soup degiskenine al
soup = BeautifulSoup(page, 'html.parser')

# cikti degiskenini bos olarak olustur
cikti = ''

# sayfanin html kodlari icinden 'inlineblock pid-50655-bid' class'ina sahip span elementini bul
for i in soup.find_all('span', {"class": "inlineblock pid-50655-bid"}):
    cikti = cikti + '\n' +  'Alis : ' + i.text	# bulunduysa, span elementinin text verisini cikti degiskeninin sonuna ekle

# sayfanin html kodlari icinden 'inlineblock pid-50655-ask' class'ina sahip span elementini bul
for i in soup.find_all('span', {"class": "inlineblock pid-50655-ask"}):
    cikti = cikti + '\n' +  'Satis : ' + i.text	# bulunduysa, span elementinin text verisini cikti degiskeninin sonuna ekle


print(cikti)	# en sonunda olusan metni ekrana bas

# olusan metni asagidaki text dosyaya yaz
with open('scraped_text.txt', 'w') as file:
    file.write(str(cikti))
