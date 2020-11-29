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
    
def Consultar_cliente():
    return(None)

def Consultar_clientes():
    return(None)
def Consultar_direccion_id():
    sucursales=dame_sucursales()
    #print(sucursales)
    idDir=int(input("dame el id de la direccion: "))
    registros=[]
    for sucursal in sucursales:
        #print(sucursal)
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
    '''if type(numero) != int and numero != ' ':
        numero=int(numero)'''
    for sucursal in sucursales:
        query=("use {}").format(sucursal)
        cursor.execute(query)
        query=("select * from Direcciones where calle like '%{}%' and numero like '{}' and colonia like '%{}%' and localidad like '%{}%' and estado like '%{}%' and CP like '%{}%' ").format(calle,numero,colonia,localidad,estado,cp)
        cursor.execute(query)
        for (idDir,calle,numero,colonia,localidad,estado,CP) in cursor:
            dire=idDir
        query=("select * from Clientes where idDir = '{}'").format(dire)
        cursor.execute(query)
        for (IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir) in cursor:
            registro2=[IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC]
            rf=(IdCli,Nombre,ApellidoPaterno,ApellidoMaterno,RFC,idDir,calle,numero,colonia,localidad,estado,CP)
            registros.append(rf)
    print(registros)
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

    
Consultar_direciones()
    
    
    
    
    
    
    
