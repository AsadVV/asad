from bs4 import BeautifulSoup
import requests

url = 'https://vgtimes.ru/games/genshin-impact/news/'

page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")




def asad():
    if page.status_code == 200:
        rr = str(soup.findAll('div', class_='shorts_new')).split('<div class="shorts_new">')

        for new in rr:
            new.split('\\n      </div>,')
            new[-14::]
            return new
            

        
        

print(asad())
