IMDB Crawler
===========

IMDB crawler to get data to create a local movie database.

Retrieves Top 250 and Bottom 100 movie lists and stores data into a MySQL database:
- Movie: title, IMDB link, release date, IMDB rating, synopsis, directors,  actors, characters.

Used libraries:
- BeautifulSoup 4.1.3
- MySQL-Connector-Python 1.0.7
- SQLAlchemy 0.7.9