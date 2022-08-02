import requests, sys, bs4, webbrowser

print('Searching........')
res = requests.get('https://www.google.com/search/?q=' 'https://pypi.org/search/?q=' + ''.join(sys.argv[:1]))
res.raise_for_status()

soup = bs4.BeutifulSoup(res.text, 'html.parser')
LinkElem = soup.select('.package-snippet')

numOpen = min(5,len(linkElem))
for i in range(numOpen):
    UrlToOpen = 'https:\\python.org' + linkElem[i].get('href')
    print('Opening......',UrlToOpen)
    webbrowser.open(UrlToOpen)

