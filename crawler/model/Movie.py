import urllib.request
from bs4 import BeautifulSoup
import time

class Movie:
    def __init__(self, imdbLink = None):
        self.ImdbLink = imdbLink
        self.parse(imdbLink)

    def parse(self, url):
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        self.Title = soup.title.string[:-14].strip()

        date = soup.find_all("span", "nobr")[1].a.string.split("(")[0][:-1].strip()
        try:
            self.ReleaseDate = time.strptime(date, '%d %B %Y')
        except ValueError:
            try:
                self.ReleaseDate = time.strptime(date, '%B %Y')
            except ValueError:
                try:
                    self.ReleaseDate = time.strptime(date, '%Y')
                except ValueError:
                    pass

        directors = soup.find_all(itemprop="director")
        self.Directors = []
        for director in directors:
            self.Directors.append(str(director.string))

        actors = soup.find('table', 'cast_list').find_all("td", "name")
        characters = soup.find('table', 'cast_list').find_all("td", "character")

        self.Actors = {}
        for i in range(len(actors)):
            characterName = characters[i].div.string

            if characterName == None:
                characterName = characters[i].div.a.string

            self.Actors[str(actors[i].a.string).strip()] = str(characterName).strip()

        #self.Characters = []
        #for character in characters:
        #    self.Characters.append(str(character.div.string).strip())

    def __repr__(self):
        return "<Movie('%s', '%s', '%s')>" % (self.ImdbLink, self.Title, self.ReleaseDate)
