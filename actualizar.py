import mariadb
#pip3 install prettytable
from prettytable import PrettyTable
import json

PATH = ''


#---------------------------------------------------
# Funciones auxiliarles

def dame_cursor_local(PATH):
    with open(PATH+'config.json') as json_file:
        config = json.load(json_file)
    cnx = mariadb.connect(**config)
    cursor = cnx.cursor()
    return cursor, cnx

def dame_sucursales():
    conn = mariadb.connect(
        user = "javo", 
        password = "b", 
        host = "127.0.0.1", 
        database = 'sucursales'
        ) 
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM nombres")
    nombres = []
    for suc in cur:
        (n,) = suc
        #n = n[0]
        nombres.append(n)
    return nombres


    
def graficar(columnas, data):
    t = PrettyTable(columnas)
    for item in data:
        t.add_row(item)
    print(t)

    
#---------------------------------------------


def actualizar(tabla):
    (cursor,cnx) = dame_cursor_local(PATH)
 
    Id = int(input('Ingrese el ID del cliente: '))
    cursor.execute('SHOW COLUMNS FROM {}'.format(tabla))
    fields = []
    for (Field,Type,Null,Key,Default,Extra) in cursor:
        if Field[:2] != 'Id':
            fields.append(Field)
    values = []
    
    print('Oprima enter si no desea cambiar el campo: ')
    for i in range(len(fields)):
        val = input('Ingrese nuevo valor de \'{}\': '.format(fields[i]))
        values.append(val)


    for i in range(len(fields)):   
        if values[i] != '':
            #cursor = dame_cursor_local(PATH)
            query = "UPDATE {} SET {} = '{}' WHERE IdCli = {}".format(tabla,fields[i],values[i],Id)
            print(query)
            cursor.execute(query)
            cnx.commit()
    
#actualizar('Clientes')
