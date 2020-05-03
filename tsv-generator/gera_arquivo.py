"""
Gera um arquivo para leitura da biblia
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
import sqlite3

def init_from_script():
    f = open('./ARA.sqlite', 'r')
    blb = f.read()
    con = sqlite3.connect("./biblia.db")
    cur = con.cursor()
    cur.executescript(blb)
    con.close()

Base = declarative_base()

class Book(Base):
    """
    CREATE TABLE IF NOT EXISTS "book" (
        "id"    INTEGER,
        "book_reference_id"     INTEGER,
        "testament_reference_id"        INTEGER,
        "name"  TEXT
        "acronym"  TEXT
    );
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    book_reference_id = Column(Integer)
    testament_reference_id = Column(Integer)
    name = Column(String)
    acronym = Column(String)

    def __repr__(self):
       return "<Book(id='%s', ref='%s', refid='%s', name='%s')>" % (
                            self.id, self.book_reference_id, self.testament_reference_id, self.name)

class Metadata(Base):
    """
    CREATE TABLE IF NOT EXISTS "metadata" (
        "key"   TEXT,
        "value" TEXT
    );
    """
    __tablename__ = 'metadata'

    key = Column(Integer, primary_key=True)
    value = Column(String)

    def __repr__(self):
       return "<Metadata(key='%s', value='%s')>" % (
                            self.key, self.value)

class Testament(Base):
    """
    CREATE TABLE IF NOT EXISTS "testament" (
            "id"    INTEGER,
            "name"  TEXT
    );
    """
    __tablename__ = 'testament'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
       return "<Testament(id='%s', name='%s')>" % (
                            self.id, self.value)


class Verse(Base):
    """
    CREATE TABLE IF NOT EXISTS "verse" (
        "id"    INTEGER,
        "book_id"       INTEGER,
        "chapter"       INTEGER,
        "verse" INTEGER,
        "text"  TEXT
    );
    """
    __tablename__ = 'verse'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String)

    book = relationship("Book")

    def __repr__(self):
       return "<Verse(id='%s', book_id='%s', chapter='%s', verse='%s', text='%s')>" % (
           self.id, self.book_id, self.chapter, self.verse, self.text)


def main():
    """
    Funcao main que executa o script
    """
    engine = create_engine('sqlite:///./ARA.sqlite', echo=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    ara_file = open('./ara.tsv', 'w')
    ara_fortune_file = open('./arafortune', 'w')

    for instance in session.query(Verse).order_by('book_id'):
        ara_file.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (instance.book.name, instance.book.acronym,
                                                      instance.book_id, instance.chapter, instance.verse, instance.text))
        ara_fortune_file.write('%s:\n%s:%s    %s\n%%\n' % (instance.book.name, instance.chapter, instance.verse, instance.text))


if __name__ == "__main__":
    main()
