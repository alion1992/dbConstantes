from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host, port):
        self.connection_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        self.engine = create_engine(self.connection_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def connect(self):

        self.session = self.Session()

    def execute_query(self, query, params=None):
        try:

            result = self.session.execute(query, params)

            return result.fetchall()
        except Exception as e:
            print("Error ejecutando la consulta:", e)
            return None
        finally:
            self.session.close()