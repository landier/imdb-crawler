import mysql.connector
from datetime import date, datetime, timedelta

class Repository:
    def __init__(self):
        self.__session = mysql.connector.connect(host='127.0.0.1',
                                                 port=8889,
                                                 database='DbSamples',
                                                 user='root',
                                                 password='root')

    def __del__(self):
        self.__session.close()

    def savePerson(self, person):
        cursor = self.__session.cursor()
        tomorrow = datetime.now().date() + timedelta(days=1)
        insert_person = ("INSERT INTO Person "
                        "(FirstName, LastName, Gender, BirthDate) "
                        "VALUES (%s, %s, %s, %s)")
        data_person = (person.FirstName, person.LastName, person.Gender, None)

        cursor.execute(insert_person, data_person)
        #emp_no = cursor.lastrowid

        self.__session.commit()
        cursor.close()

    def saveMovie(self, movie):
        cursor = self.__session.cursor()
        tomorrow = datetime.now().date() + timedelta(days=1)
        insert_movie = ("INSERT INTO Movie "
                         "(Title, Year, ImdbLink) "
                         "VALUES (%s, %s, %s)")
        data_movie = (movie.Title, movie.Year, movie.ImdbLink)

        cursor.execute(insert_movie, data_movie)
        #emp_no = cursor.lastrowid

        self.__session.commit()
        cursor.close()
