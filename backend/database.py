# database.py
import psycopg2
from decouple import config


def connect_to_database():
    try:
    #? Configurar la conexión a la base de datos
        connection = psycopg2.connect(
            database=config("DB_DATABASE"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            port=config("DB_PORT")
        )
        print("---- Conexión exitosa ----")
        
        return connection
    except psycopg2.Error as e:
        print("---- Error en la conexión ----")

# print(config("DB_DATABASE"),config("DB_USER"))
# connect_to_database()

def execute_query():
    connection = connect_to_database()
    # Ejecutar la consulta
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks;")
    result = cursor.fetchall()
    return result


# def execute_query_with_return(connection, query):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query)
#     connection.commit()
#     return cursor.fetchall()

# def execute_query_with_return_one(connection, query):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query)
#     connection.commit()
#     return cursor.fetchone()

# def execute_query_with_return_one_with_params(connection, query, params):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query, params)
#     connection.commit()
#     return cursor.fetchone()


# def execute_query_with_return_many(connection, query, params):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query, params)
#     connection.commit()
#     return cursor.fetchall()

# def execute_query_with_return_many_with_params(connection, query, params):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query, params)
#     connection.commit()
#     return cursor.fetchall()

# def execute_query_with_return_many_with_params_and_limit(connection, query, params, limit):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query, params)
#     connection.commit()
#     return cursor.fetchmany(limit)

# def execute_query_with_return_many_with_params_and_limit_and_offset(connection, query, params, limit, offset):
#     # Ejecutar la consulta
#     cursor = connection.cursor()
#     cursor.execute(query, params)
#     connection.commit()
#     return cursor.fetchmany(limit, offset)