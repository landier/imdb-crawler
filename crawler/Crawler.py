from crawler.Movie import Movie
import urllib.request
from crawler.Repository import Repository
from bs4 import BeautifulSoup

URL_TOP_250 = 'http://www.imdb.com/chart/top'
URL_BOTTOM_100 = 'http://www.imdb.com/chart/bottom'
ROOT_URL =  'http://www.imdb.com'

repository = Repository()

response = urllib.request.urlopen(URL_BOTTOM_100)
html = response.read()
soup = BeautifulSoup(html)

movieList = soup.table.find_all("a")

for element in movieList:
    movie = Movie()
    movie.parse(ROOT_URL+element['href'])
    repository.saveMovie(movie)

#print(soup.find_all('a', 'href'))

#for element in movieList.next_siblings:
 #   print(element)

#movie = Movie()
#movie.parse('http://www.imdb.com/title/tt0440963/')
#movie.show()

#repository.saveMovie(movie)