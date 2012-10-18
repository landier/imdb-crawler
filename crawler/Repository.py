from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine

class Repository:
    def __init__(self, showLog = False):
        self.__showLog = showLog
        self.__engine = create_engine('mysql+mysqlconnector://root:root@localhost:8889/MovieDB', echo=self.__showLog)
        self.__metadata = MetaData()

        self.__persons = Table('Person', self.__metadata,
            Column('Id', Integer, primary_key=True),
            Column('Name', String(50))
        )

        self.__movies = Table('Movie', self.__metadata,
            Column('Id', Integer, primary_key=True),
            Column('Title', String(255), nullable=False)
        )

        self.__actors = Table('Actor', self.__metadata,
            Column('Id', Integer, primary_key=True),
            Column('Person_id', None, ForeignKey('Person.Id')),
            Column('Movie_id', None, ForeignKey('Movie.Id')),
            Column('Character', String(50), nullable=False)
        )

        self.__directors = Table('Director', self.__metadata,
            Column('Id', Integer, primary_key=True),
            Column('Person_id', None, ForeignKey('Person.Id')),
            Column('Movie_id', None, ForeignKey('Movie.Id'))
        )

    def createSchema(self):
        self.__metadata.create_all(self.__engine)

    def insertPerson(self, name):
        ins = self.__persons.insert().values(Name=name)

        if self.__showLog:
            ins.bind = self.__engine
            print(str(ins))

        ins.compile().params
        conn = self.__engine.connect()
        conn
        result = conn.execute(ins)

        result.inserted_primary_key

    def insertMovie(self, title):
        ins = self.__movies.insert().values(Title=title)

        if self.__showLog:
            ins.bind = self.__engine
            print(str(ins))

        ins.compile().params
        conn = self.__engine.connect()
        conn
        result = conn.execute(ins)

        result.inserted_primary_key