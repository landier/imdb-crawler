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

        self.Title = soup.title.string[:-14]
        self.Year = soup.title.string[:-8][-4:]
        date = soup.find_all("span", "nobr")[1].a.string.split("(")[0][1:][:-1]
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

        actors = soup.find('table', 'cast_list').find_all("td", "name")
        self.Actors = []
        for actor in actors:
            self.Actors.append(str(actor.a.string))

        self.Characters = soup.find('table', 'cast_list').find_all("td", "character")
        #for character in characters:
        #    print(character.div.string)

    def __repr__(self):
        return "<Movie('%s', '%s', '%s')>" % (self.ImdbLink, self.Title, self.ReleaseDate)
