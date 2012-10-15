import urllib.request
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, title = None, year = None, imdbLink = None):
        self.ImdbLink = imdbLink
        self.Title = title
        self.Year = year
        self.Actors = None
        self.Characters = None

    def parse(self, url):
        self.ImdbLink = url
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        self.Title = soup.title.string[:-14]
        self.Year = soup.title.string[:-8][-4:]
        #print(soup.find('table', 'cast_list'))
        #self.__actors = soup.find_all('td', 'name')
        #self.__characters = soup.find_all('td', 'character')

    def show(self):
        print(self.ImdbLink)
        print(self.Title)
        print(self.Year)

        #print(self.__actors[0])
        #result = re.match(r'">(.*)<', actors[0])
        #print(self.__characters[0])
        #print(self.__actors[1])
        #print(self.__characters[1])
