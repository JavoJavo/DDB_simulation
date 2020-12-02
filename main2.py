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
    return cursor

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
    '''
    row_format ="{:>15}" * (len(columnas) + 1)
    print(row_format.format("", *columnas))
    for team, row in zip(columnas, data):
        print(row_format.format(team, *row))
    '''
    

#-------------------------------------------------------------------
# insertar
def insertar():
    
    sucs = dame_sucursales()
    i = 0
    for s in sucs:
        print(i,s)
        i += 1
    suc = int(input('Elige sucursal: '))
    bd = sucs[suc]
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
    menu()
#--------------------------------------------------------------------
# actualizar
    
def actualizarUsuario():
    print('Funcion pendiente')
    menu()

    
def actualizarDireccion(a, info):
    print('Funcion pendiente')
    menu()
#--------------------------------------------------------------------
# consultar


def Consultar_cliente(nombre,apellido1,apellido2):
    cursor = dame_cursor_local(PATH)
    sucursales=dame_sucursales()
    registros=[]
    datos=[nombre,apellido1,apellido2]
    idD=[]
    for i in range(len(datos)):
        if datos[i] == '':
            datos[i] = '%%'
        else:
            datos[i] = '%'+datos[i]+'%'
    nombre=datos[0]
    apellido1=datos[1]
    apellido2=datos[2]
    for sucursal in sucursales:
        idD=0#[]
        query=("use {}").format(sucursal)
        cursor.execute(query)
        query=("select * from Clientes where Nombre like '{}' and ApellidoPaterno like '{}' and ApellidoMaterno like '{}'").format(nombre,apellido1,apellido2)
        cursor.execute(query)
        print('paso')
        for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
            r1=[]
            idD=idDir
            print(idD)
        query=("select * from Direcciones where idDir = {} ").format(idD)
        print(query)
        cursor.execute(query)
        print('pasoasdfa')
        for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
            r2=[]
        rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
        registros.append(rf)
    return(registros)
        
        
def consultaFacil():
    cursor = dame_cursor_local(PATH)
    print("tienes el id o el RFC?")
    print("1.- ID")
    print("2.- RFC")
    a=int(input())
    sucursales=dame_sucursales()
    registros=[]
    idD=None
    if a ==1:
        iD=input("dame el id: ")
        for sucursal in sucursales:
            query=("use {}").format(sucursal)
            cursor.execute(query)
            query=("select * from Clientes where idCli = {}").format(iD)
            cursor.execute(query)
            for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
                r1=[]
                idD=idDir
            query=("select * from Direcciones where idDir = {} ").format(idD)
            cursor.execute(query)
            for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
                r2=[]
            rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
            registros.append(rf)
        return(registros)
    if a == 2:
        iD=input("dame el RFC: ")
        for sucursal in sucursales:
            query=("use {}").format(sucursal)
            cursor.execute(query)
            query=("select * from Clientes where RFC = '{}' ").format(iD)
            cursor.execute(query)
            for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
                r1=[]
                idD=idDir
            query=("select * from Direcciones where idDir = {} ").format(idD)
            cursor.execute(query)
            for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
                r2=[]
            rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
            registros.append(rf)
        return(registros)
            
    
def Consultar_clientes():
    columnas = ['IdCli','Nombre','Apellido1','Apellido2','RFC','IdDir', 'Calle', 'Numero','Colonia','Localidad','Estado','CP']
    print("¿tienes el id del cliente o el rfc?")
    print("1.- si")
    print("2.- No")
    a=int(input())
    if a == 1:
        data=consultaFacil()
        graficar(columnas, data)
    if a == 2:
        nombre=input("dame el nombre o nombres,si no lo sabe de enter")
        apellido1=input("dame el primer apellido, si no lo sabe de enter")
        apellido2=input("dame el segundo apellido, si no lo sabe de enter")
        data=Consultar_cliente(nombre,apellido1,apellido2)
        graficar(columnas,data)
        
def Consultar_direccion_id():
    cursor = dame_cursor_local(PATH)
    sucursales=dame_sucursales()
    idDir=int(input("dame el id de la direccion: "))
    registros=[]
    for sucursal in sucursales:
        query=("use {}").format(sucursal)
        cursor.execute(query)
        query=("select * from Direcciones where idDir = {}").format(idDir)
        cursor.execute(query)
        for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
            registro1=[calle,numero,colonia,localidad,estado,CP]
        query=("select * from Clientes where idDir = {}").format(idDir)
        cursor.execute(query)
        for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
            registro2=[IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC]
        rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
        registros.append(rf)
    return(registros)
        
        
def Consultar_direccion_noID(calle,numero,colonia,localidad,estado,cp):
    cursor = dame_cursor_local(PATH)
    sucursales=dame_sucursales()
    registros=[]
    dire=None
    datos=[calle,numero,colonia,localidad,estado,cp]
    for i in range (len(datos)):
        if datos[i] == '':
            datos[i] = '%%'
        elif datos[i] != '':
            datos[i] = '%'+datos[i]+'%'
    calle=datos[0]
    numero=datos[1]
    colonia=datos[2]
    localidad=datos[3]
    estado = datos[4]
    cp= datos[5]
    for sucursal in sucursales:
        query=("use {}").format(sucursal)
        cursor.execute(query)
        query=("select * from Direcciones where calle like '{}' and numero like '{}' and colonia like '{}' and localidad like '{}' and estado like '{}' and CP like '{}' ").format(calle,numero,colonia,localidad,estado,cp)
        cursor.execute(query)
        for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
            dire=idDir
        query=("select * from Clientes where idDir = '{}'").format(dire)
        cursor.execute(query)
        for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
            registro2=[IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC]
            rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
            registros.append(rf)
    return(registros)
    
def Consultar_direciones():
    columnas = ['IdCli','Nombre','Apellido1','Apellido2','RFC','IdDir', 'Calle', 'Numero','Colonia','Localidad','Estado','CP']
    print("sabe la id de la direccion?")
    print("1.- Si")
    print("2.- No")
    a=int(input())
    if a == 1:
        data=Consultar_direccion_id()
        graficar(columnas, data)
    if a == 2:
        calle=input("ingrese la calle, si no la sabe de enter")
        numero=input("ingrese el numero, si no lo sabe de enter")
        colonia=input("ingrese la colonia, si no la sabe de enter")
        localidad=input("ingrese la localidad, si no la sabe de enter")
        estado=input("ingrese el estado, si no lo sabe de enter")
        cp=input(" ingrese el CP, si no lo sabe de enter")
        data=Consultar_direccion_noID(calle,numero,colonia,localidad,estado,cp)
        graficar(columnas, data)

    
#--------------------------------------------------------------------
# Crear tabla

def CrearTabla():
    print('Funcion pendiente')
    menu()
    
def ponTipoDato():
    print('Inserta el tipo de dato: ')
    print('Ej.1: INT NOT NULL AUTO_INCREMENT')
    print('Ej.2: VARCHAR(100)')

    tipo = input()
    
    return tipo
    
def CrearTablaLocal():
    with open(PATH+'config.json') as json_file:
        config = json.load(json_file)
    cnx = mariadb.connect(**config)
    cursor = cnx.cursor()
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
    print ('Query:',query)
    cursor.execute(query)
    cursor.close()
    
#--------------------------------------------------------------------
# Interfaz principal
'''def mainActualizar():
    print("¿Que tipo de registro quiere actualizar?")
    print("1.- usuario")
    print("2.- direccion")
    a=int(input())
    if a == 1:
        actualizarUsuario()
    if a == 2:
        actualizarDireccion()
    else:
        print("opcion invalida, vuelve a intentarlo")
        mainActualizar()'''
        

def verificador(a,info):
    if a == 1:
        print("la direccion es ",info, "¿continuar?")
        print("1.- si")
        print("2.- cambiar")
        opcion=int(input())
        if opcion == 1:
            Consultar_direciones(a,info)
        elif opcion == 2:
            print("ingrese la nueva informacion")
            info=input()
            verificador(a,info)
        else:
            print("opcion invalida")
            verificador(a,info,opcion)
        menu()
    if a == 2:
        print("el rfc es ",info, "¿continuar?")
        print("1.- si")
        print("2.- cambiar")
        opcion=input()
        if opcion == '1':
            Consultar_clientes('RFC',info)
        elif opcion == '2':
            print("ingrese la nueva informacion")
            info=input()
            verificador(a,info)
        else:
            print("opcion invalida")
            verificador(a,info)
        menu()
    if a == 3:
        print("el nombre que quiere buscar es: ",info," ","¿Continuar?")
        print("1.- si")
        print("2.- cambiar")
        opcion=int(input())
        if opcion == 1:
            Consultar_clientes('Nombre',info)
        elif opcion == 2:
            print("ingrese la nueva informacion")
            info=input()
            verificador(a,info)
        else:
            print("opcion invalida")
            verificador(a,info)
        menu()


'''def mainConsultarTodo():
    print("¿Con que dato desea consultar?")
    print("1.- Direcion")
    print("2.- Nombre o RFC")
    a=int(input())
    if a == 1:
        Consultar_direciones()
    elif a == 2:
        Consultar_clientes()'''


def mainListar(opcion):
    opciones=["Actualizar informacion","Consultar informacion","Crear Un Nuevo Registro"]
    lista=[]
    diccionario={}
    with open(PATH+'config.json') as jfile:
        data=json.load(jfile)
        db=data['database']
    query=("select table_name from information_schema.columns where table_schema = '{}' order by table_name, ordinal_position").format(db)
    cursor.execute(query)
    for i in cursor:
        lista.append(i)
    lista=list(set(lista))
    print("en donde quieres",opciones[opcion])
    for i in range(len(lista)):
        print(i, lista[i][0])
        diccionario[i]=lista[i][0]
    seleccion=int(input())
    if diccionario[seleccion] == 'Clientes' or diccionario[seleccion] == 'Direcciones' :
        if opcion ==0:
            print(diccionario[seleccion])
            actualizar(diccionario[seleccion])
        if opcion ==1 diccionario[seleccion] == 'Clientes':
            Consultar_clientes()
        if opcion == 1 and diccionario[seleccion] == 'Direcciones':
            Consultar_direciones()
        if opcion ==2:
            insertar()
    else:
        if opcion== 0:
            actualizar(diccionario[seleccion])
        if opcion==1:
            consGen(diccionario[seleccion])
        if opcion ==2:
            insertarGen(diccionario[seleccion])

def consGen(tabla):
    iD= int(input("Dame el id del cliente"))
    cursor.execute('SHOW COLUMNS FROM {}'.format(tabla))
    fields = []
    registros=[]
    res=[]
    for (Field,Type,Null,Key,Default,Extra) in cursor:
        fields.append(Field)
    for i in range(len(fields)):
        query=("select {} from {} where IdCli = {}").format(fields[i],tabla,iD)
        cursor.execute(query)
        registro=[]
        for i in cursor:
            registro.append(i[0])
        registros.append(registro)
    for i in range(len(registros[0])):
        re=[]
        for j in range(len(registros)):
            re.append(registros[j][i])
        res.append(re)
    return(re)


def main():
    print("1.- Actualizar informacion")
    print("2.- Consultar informacion")
    print("3.- Crear Nuevo Registro")
    print("4.- Crear nueva tabla")
    print("5.- Salir")
        
def menu():
    main()
    opcion=int(input("¿que desea hacer? "))
    if opcion == 1:
        #mainActualizar()
        mainListar(0)
    elif opcion == 2:
        #mainConsultarTodo()
        mainListar(1)
    elif opcion == 3:
        #insertar()
        mainListar(2)
    elif opcion == 4:
        CrearTablaLocal()
    elif opcion == 5:    
        exit()
    else:
        print("opcion invalida, vuelve a intentarlo")
          
menu()
