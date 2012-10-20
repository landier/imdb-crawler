import urllib
from bs4 import BeautifulSoup
from multiprocessing import Pool
from crawler.Repository import Repository
from crawler.model.Movie import Movie

URL_TOP_250 = 'http://www.imdb.com/chart/top'
URL_BOTTOM_100 = 'http://www.imdb.com/chart/bottom'
ROOT_URL =  'http://www.imdb.com'
NUMBER_OF_THREADS = 10

def retrieveAndSaveMovieData(url):
    movie = Movie(ROOT_URL + url)
    repository.saveMovie(movie)

def retrieveMovieList(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)

    movieList = soup.table.find_all("a")

    p = Pool(NUMBER_OF_THREADS)

    movieListUrl = []
    for movie in movieList:
        movieListUrl.append(movie['href'])
    # To debug, uncomment the following line...
    #    retrieveAndSaveMovieData(movie['href'])

    # ... and comment the following line.
    p.map(retrieveAndSaveMovieData, movieListUrl)

repository = Repository()
retrieveMovieList(URL_TOP_250)
retrieveMovieList(URL_BOTTOM_100)
