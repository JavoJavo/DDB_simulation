from prettytable import PrettyTable
import json
#import mysql.connector
import mariadb
PATH=''
#if __name__ == "__main__":
with open(PATH+'config.json') as json_file:
    config = json.load(json_file)
cnx = mariadb.connect(**config)
cursor = cnx.cursor()
#    query1=("CREATE TABLE Direcciones (IdDir INT NOT NULL AUTO_INCREMENT,calle VARCHAR(100),numero VARCHAR(50),colonia VARCHAR(100),localidad VARCHAR(100),estado VARCHAR(50),CP CHAR(5),PRIMARY KEY(IdDir))")
#    query2=("CREATE TABLE Clientes (IdCli INT NOT NULL AUTO_INCREMENT, Nombre VARCHAR(50),ApellidoPaterno VARCHAR(50),ApellidoMaterno VARCHAR(50),RFC CHAR(13),IdDir INT,PRIMARY KEY (IdCli),FOREIGN KEY (IdDir) REFERENCES Direcciones(IdDir))")


def ponTipoDato():
    print('Inserta el tipo de dato: ')
    print('Ej.1: INT NOT NULL AUTO_INCREMENT')
    print('Ej.2: VARCHAR(100)')

    tipo = input()
    
    return tipo
    
def CrearTablaLocal():
    #cursor.execute('USE prueba')
    nombre = input('Nombre de la nueva tabla: ')
    campos = []
    tipos = []
    query = 'CREATE TABLE ' + nombre + ' ('
    print('Inserta los campos:')
    while True:
        campo = (input('Nombre del campo: '))
        tipo = (ponTipoDato())
        query += campo +' '+ tipo + ','
        termina = int(input('Agregar otro campo? si:1 , no:2  :'))
        if termina == 2:
            break
        
    query += 'IdCli INT, FOREIGN KEY (IdCli) REFERENCES Clientes(IdCli))'
    #query = query[:len(query)-1] + ')'
    #query += ')'
    print ('Query:',query)
    cursor.execute(query)

CrearTablaLocal()
