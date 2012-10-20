import urllib
from bs4 import BeautifulSoup
from multiprocessing import Pool
from crawler.Repository import Repository
from crawler.model.Movie import Movie

URL_TOP_250 = 'http://www.imdb.com/chart/top'
URL_BOTTOM_100 = 'http://www.imdb.com/chart/bottom'
ROOT_URL =  'http://www.imdb.com'

def getAndSaveMovieData(url):
    movie = Movie(ROOT_URL + url)
    movieId = repository.saveMovie(movie)

    for directorName in movie.Directors:
        repository.saveDirector(movieId, directorName)

    for actorName, characterName in movie.Actors.items():
        repository.saveActor(movieId, actorName, characterName)

repository = Repository()

response = urllib.request.urlopen(URL_TOP_250)
html = response.read()
soup = BeautifulSoup(html)

movieList = soup.table.find_all("a")

for element in movieList:
    getAndSaveMovieData(element['href'])

