import os
import mariadb
#from m import errorcode

usuario=input("introduzca un usuario registrado con derechos de crear bases de datos: ")
passw=input("introduzca la clave de autentificacion para dicho usuario: ")

def meterRegistros(usuario,clave):
    cnx=mariadb.connect(host='localhost',user=usuario, passwd=clave,)
    cursor=cnx.cursor()
    query=("use Morelia")
    query1=("CREATE TABLE Direcciones (IdDir INT NOT NULL AUTO_INCREMENT,calle VARCHAR(100),numero VARCHAR(50),colonia VARCHAR(100),localidad VARCHAR(100),estado VARCHAR(50),CP CHAR(5),PRIMARY KEY(IdDir))")
    query2=("CREATE TABLE Clientes (IdCli INT NOT NULL AUTO_INCREMENT, Nombre VARCHAR(50),ApellidoPaterno VARCHAR(50),ApellidoMaterno VARCHAR(50),RFC CHAR(13),IdDir INT,PRIMARY KEY (IdCli),FOREIGN KEY (IdDir) REFERENCES Direcciones(IdDir))")
    query3=("INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('San Benito', '556', 'Armando Madero','Morelia', 'Michoacán', '54954'),('Cristobal Colón',  '84', 'Avante', 'Maravatío', 'Michoacán', '51682'),('Leona Vicario',  '68B', 'Josefa Ortiz de Dominquez', 'Morelia', 'Michoacán', '56921'),('Paseo de la República',  '599', 'Soledad', 'Morelia', 'Michoacán', '58088'),('Villa Olímpica','775','Valladolid','Morelia','Michoacán','45444')")
    query4=("INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Javier','Navarro','Espindola','VECJ880326001',1),('Armando','Villicaña','Gameza','VECJ880326801',4),('Karla','Herrera','Bilk','VECJ880326061',2),('Mario','Nuñez','Vizicalla','VECJ880326701',5),('Angela','Ornelas','Ceja','VECJ880326031',3)")
    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cnx.commit()
    cursor.execute(query4)
    cnx.commit()
    query11=("use Pátzcuaro")
    query12=("INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Batalla de Naco', '741', 'Juárez','Pátzcuaro', 'Michoacán', '54154'),('La otra banda',  '15', 'Roma', 'Pátzcuaro', 'Michoacán', '11681'),('Piedra del Comal',  '11', 'Polanco', 'Pátzcuaro', 'Michoacán', '51121'),('Balcón de los edecanes',  '48', 'Tlatelolco', 'Pátzcuaro', 'Michoacán', '58008'),('Rayando el sol','747','Del Carmen','Pátzcuaro','Michoacán','45400')")
    query13=("INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Hugo','Acosta','Acuña','VECS880326001',1),('Lucía','Aguilar','Aguirre','VECS880326801',2),('Daniel','Agustín','Ahumada','VECS880326061',3),('Martina','Alanis','Alarcón','VECS880326701',5),('Alejandro','Alayón','Alcázar','VECS880326031',4)")
    
    
    cursor.execute(query11)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query12)
    cnx.commit()
    cursor.execute(query13)
    cnx.commit()
    cnx.close()
    
def conectar(usuario,clave):
    try:
        cnx=mariadb.connect(host='localhost',user=usuario, passwd=clave,)
        cursor=cnx.cursor()
        query=("CREATE DATABASE Morelia ")
        query1=("CREATE DATABASE Pátzcuaro")
        query2=("CREATE DATABASE sucursales")
        query3=("CREATE TABLE nombres (n VARCHAR(100))")
        query4=("INSERT INTO nombres (n) VALUES ('Morelia'),('Pátzcuaro')")
        cursor.execute(query)
        print(1)
        cursor.execute(query1)
        print(2)
        cursor.execute(query2)
        print(3)
        cursor.execute('USE sucursales')
        cursor.execute(query3)
        print(4)
        cursor.execute(query4)
        print(5)
        cnx.commit()
        cnx.close()
        meterRegistros(usuario,clave)
        
        print('Operacion exitosa!')

    except: #mariadb.Error as err:
        print('Hubo un error')
        '''
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("algo esta mal con tu usuario o contrasena")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("la base de datos no existe")
        else:
            print(err)
    else:
        cnx.close()
        '''


conectar(usuario,passw)
