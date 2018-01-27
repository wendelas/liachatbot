import sqlite3

class con():
    def __init__(self):
        """
        Construct of the class, create all table of brain
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()

        # criando a table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pattern(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            pattern text not NULL,
            section integer not NULL
        );
        """)
        # criando a table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS response(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            response text not NULL,
            patternId integer not NULL
        );
        """)

        print("Brain iniciado com sucesso...")
        conn.close()

    def query(self,sql):
        """
        Execute a query in sqlite
        :param sql: String
        :return: Boolean
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.close()
        return True

    def insertPattern(self,pattern,section):
        """
        Insert a new pattern in knowledge
        :param pattern: String
        :param section: Integer
        :return: Integer
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pattern(pattern,section) VALUES('"+pattern+"',"+str(section)+");")
        conn.commit()
        cursor.execute("SELECT id FROM pattern ORDER BY id DESC")
        patternid = cursor.fetchone()[0]
        conn.close()
        return patternid

    def insertResponse(self,response,patternId):
        """
        Insert a new response in knowledge
        :param pattern: String
        :param section: Integer
        :return: Boolean
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO response(response,patternId) values('"+response+"',"+str(patternId)+");")
        conn.commit()
        conn.close()
        return True

    def getAllPatternSection(self,section):
        """
        Get all pattern of the section aim
        :param section: Int
        :return: List
        """
        aux = []
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pattern WHERE section like "+str(section)+";")
        for linha in cursor.fetchall():
            aux.append(linha)
        conn.close()
        return aux


    def getAllResponsePattern(self,pattern):
        """
        Get all pattern of the section aim
        :param section: Int
        :return: List
        """
        aux = []
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM response WHERE patternId like "+str(pattern)+";")
        for linha in cursor.fetchall():
            aux.append(linha)

        conn.close()
        return aux

    def getResponse(self,id):
        """
        Get a response of index id
        :param id: Integer
        :return: Tuple
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM response WHERE id like " + str(id) + ";")
        aux = cursor.fetchone()
        conn.close()
        return aux

    def getPattern(self,id):
        """
        Get a pattern of index id
        :param id: Integer
        :return: Tuple
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pattern WHERE id like " + str(id) + ";")
        aux = cursor.fetchone()
        conn.close()
        return aux