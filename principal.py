import constantes as cons
import db
from sqlalchemy import  text
def conexion ():
    db_config = {
        'dbname': cons.dbname,
        'user': cons.user,
        'password': cons.password,
        'host': cons.host,
        'port': cons.port,
    }
    return db_config

def crearConexion():
    db_config = conexion()
    db_connection = db.PostgreSQLConnection(**db_config)
    db_connection.connect()
    return db_connection

if __name__ == "__main__":
    db_connection = crearConexion()
    query = text(cons.QUERY_SELECT_BY_ID)
    result = db_connection.execute_query(query,{'id': 3})
    print(result)





