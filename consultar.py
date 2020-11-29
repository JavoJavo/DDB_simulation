from prettytable import PrettyTable
import json
import mysql.connector
PATH='/home/saul/Escritorio/'
if __name__ == "__main__":
    with open(PATH+'config.json') as json_file:
        config = json.load(json_file)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
def graficar(columnas, data):
    t = PrettyTable(columnas)
    for item in data:
        t.add_row(item)
    print(t)

def dame_sucursales():
    nombres = []
    cursor.execute("use sucursales")
    cursor.execute("SELECT * FROM nombres")
    for suc in cursor:
        (n,) = suc
        nombres.append(n)
    return nombres
    
def Consultar_cliente(nombre,apellido1,apellido2):
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
        idD=[]
        query=("use {}").format(sucursal)
        cursor.execute(query)
        query=("select * from Clientes where Nombre like '{}' and ApellidoPaterno like '{}' and ApellidoMaterno like '{}'").format(nombre,apellido1,apellido2)
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
        
        
def consultaFacil():
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
    #print(registros)
    return(registros)
        
        
def Consultar_direccion_noID(calle,numero,colonia,localidad,estado,cp):
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
        #print(cursor)
        for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
            dire=idDir
        query=("select * from Clientes where idDir = '{}'").format(dire)
        cursor.execute(query)
        for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
            registro2=[IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC]
            rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
            registros.append(rf)
    #print(registros)
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

    
#Consultar_direciones()

#Consultar_clientes()
    
    
    
    
    
    
