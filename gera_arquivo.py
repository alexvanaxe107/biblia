"""
Gera um arquivo para leitura da biblia
"""
from sqlalchemy import create_engine
import sqlite3

def init_from_script():
    f = open('./ARA.sqlite', 'r')
    blb = f.read()
    con = sqlite3.connect("./biblia.db")
    cur = con.cursor()
    cur.executescript(blb)
    con.close()

def main():
    """
    Funcao main que executa o script
    """
    init_from_script()

if __name__ == "__main__":
    main()
