import urllib
from bs4 import BeautifulSoup
from crawler.Repository import Repository
from crawler.model.Movie import Movie

URL_TOP_250 = 'http://www.imdb.com/chart/top'
URL_BOTTOM_100 = 'http://www.imdb.com/chart/bottom'
ROOT_URL =  'http://www.imdb.com'

repository = Repository()

response = urllib.request.urlopen(URL_BOTTOM_100)
html = response.read()
soup = BeautifulSoup(html)

movieList = soup.table.find_all("a")

for element in movieList:
    movie = Movie(ROOT_URL + element['href'])
    movie.show()
    repository.insertMovie(movie.Title)