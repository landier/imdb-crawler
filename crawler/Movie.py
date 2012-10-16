import urllib.request
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, imdbLink = None):
        self.ImdbLink = imdbLink
        self.parse(imdbLink)

    def parse(self, url):
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        self.Title = soup.title.string[:-14]
        self.Year = soup.title.string[:-8][-4:]
        self.ReleaseDate = soup.find_all("span", "nobr")[1].a.string.split("(")[0][:-1]

        self.Actors = soup.find('table', 'cast_list').find_all("td", "name")
        #for actor in actors:
        #   print(actor.a.string)

        self.Characters = soup.find('table', 'cast_list').find_all("td", "character")
        #for character in characters:
        #    print(character.div.string)

    def show(self):
        print(self.ImdbLink)
        print(self.Title)
        print(self.Year)

        #print(self.__actors[0])
        #result = re.match(r'">(.*)<', actors[0])
        #print(self.__characters[0])
        #print(self.__actors[1])
        #print(self.__characters[1])
