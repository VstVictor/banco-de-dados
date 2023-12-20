
# conexão com banco de dados
# pip install mysql-connector-python para estabelecer a conexão

import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        dbconfig = {
            'host': '127.0.0.1',
            'user': 'Python',
            'password': 'Python21',
            'database': 'escola',
        }

        con = mysql.connector.connect(**dbconfig)
        return con
    except (Exception, Error) as error:
        print('Não conectou! ' + str(error))


def read(con):
    cursor = con.cursor()

    query = '''SELECT * FROM estudante;'''

    try:
        cursor.execute(query)

        print('\n\t\t\t ** SENAI - LISTA DE CHAMADA ** ')
        print('\t --- Matrícula --- \t ---- Nome ---')
        for campo in cursor.fetchall():
            print(f'\t\t {campo[0]} \t\t\t {campo[1]}')

    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        cursor.close()


def create(con, estudante):
    cursor = con.cursor()

    query = '''INSERT INTO estudante(matrícula, nome) VALUES(%s, %s);'''

    try:
        cursor.executemany(query, estudante)
        con.commit()
    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        cursor.close()


def update(con, estudante):
    cursor = con.cursor()

    query = '''UPDATE estudante SET nome = %s WHERE matrícula = %s;'''

    try:
        cursor.executemany(query, estudante)
        con.commit()
    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        cursor.close()


def delete(con, estudante):
    cursor = con.cursor()

    query = '''DELETE FROM estudante WHERE matrícula = %s;'''

    try:
        cursor.executemany(query, estudante)
        con.commit()
    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        cursor.close()


# Teste

con = conectar()
create(con, [('23456789', 'Maria')])
read(con)
# update(con, [('Pedro', '23456789')])
# read(con)
# delete(con, [('23456789')])
# read(con)
con.close()  # Fechar a conexão apenas no final
