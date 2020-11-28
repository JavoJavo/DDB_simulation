import mariadb 

    


def insertar(bd):
    
    print('Inserta datos personales:')
    
    nombre = input('Nombre: ')
    apellidoP = input('Apellido paterno: ')
    apellidoM = input('Apellido materno: ')
    RFC =  input('RFC (13 digitos): ')
    while (len(RFC) != 13):
        RFC =  input('RFC (13 digitos): ')
        
    print('Inserta direccion:')
    
    calle = input('Calle: ')
    numero = input('Numero: ')
    colonia = input('Colonia: ')
    localidad = input('Localidad: ')
    estado = input('Estado: ')
    CP = input('Codigo postal: ')
    while (len(CP) != 5):
        CP = input('Codigo postal: ')

    
    conn = mariadb.connect(
        user = "javo", 
        password = "b", 
        host = "127.0.0.1", 
        database = bd
        ) 

    cur = conn.cursor()
    cur.execute("INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('{}', '{}', '{}','{}', '{}', '{}');".format(calle, numero, colonia, localidad, estado,CP))
    conn.commit()
    
    
    cur = conn.cursor()
    cur.execute(" SELECT IdDir FROM Direcciones ORDER BY IdDir DESC LIMIT 1")
    (IdDir,) = cur
    IdDir = IdDir[0]
    
    cur.execute("INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('{}','{}','{}','{}','{}');".format(nombre, apellidoP, apellidoM, RFC,IdDir))
    conn.commit()

    conn.close()
    
    
#insertar('prueba')
