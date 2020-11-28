import mariadb
#pip3 install prettytable
from prettytable import PrettyTable

#---------------------------------------------------
# Funciones auxiliarles

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

def consultar(a,info):
    print('Funcion pendiente')
    menu()

def consultar_cliente(bd,atributo, value):
    
    
    conn = mariadb.connect(
        user = "javo", 
        password = "b", 
        host = "127.0.0.1", 
        database = bd
        ) 
    
    IdDir = 0 # para que no truene en caso de consulta vacia
    
    if atributo == 'Nombre' or atributo == 'ApellidoPaterno' or atributo == 'ApellidoMaterno' or atributo == 'RFC' or atributo == 'IdCli':
        data = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM Clientes WHERE {} = '{}'".format(atributo, value))
        for tupla in cur:
            (IdCi,n,aM,aP,RFC,IdDir) = tupla
            data.append([IdCi,n,aM,aP,RFC,IdDir])
            #print(IdCi,n,aM,aP,RFC,IdDir)#, end = '')
        
        #i = 0
        for i in range(len(data)):
            cur.execute("SELECT * FROM Direcciones WHERE IdDir = '{}'".format(data[i][5]))#IdDir))
            for tupla in cur:
                (IdDir,ca,num,col,loc,est,CP) = tupla
                data[i] = data[i] + [ca,num,col,loc,est,CP]
                #print(IdDir,ca,num,col,loc,est,CP)
                #i += 1
        
        conn.close()
        return(data)
    
    
    else:
        #print('paso')
        data = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM Direcciones WHERE {} = '{}'".format(atributo, value))
        for tupla in cur:
            (IdDir,ca,num,col,loc,est,CP) = tupla
            data.append([IdDir,ca,num,col,loc,est,CP])
            #print(IdDir,ca,num,col,loc,est,CP)
        
        #i = 0
        #while i < len(data):
        for i in range(len(data)):
            cur.execute("SELECT * FROM Clientes WHERE IdDir = '{}'".format(data[i][0]))
            tuplas = []
            for tupla in cur:
                (IdCi,n,aM,aP,RFC,IdDir) = tupla
                data[i] = [IdCi,n,aM,aP,RFC] + data[i]
                #print(IdCi,n,aM,aP,RFC,IdDir)
                #i = i +1
                #print(i)
        conn.close()
        return (data)


def Consultar_clientes(atributo,valor):
    columnas = ['IdCli','Nombre','Apellido1','Apellido2','RFC','IdDir', 'Calle', 'Numero','Colonia','Localidad','Estado','CP']
    sucs = dame_sucursales()
    data = []
    
    for suc in sucs:
        registros = consultar_cliente(suc,atributo,valor)
        data = data + registros
        #print(data)
    #for d in data:
        #print(d)
        #None
    graficar(columnas, data)

#--------------------------------------------------------------------
# Interfaz principal
def mainActualizar():
    print("¿Que tipo de registro quiere actuslizar?")
    print("1.- usuario")
    print("2.- direccion")
    a=int(input())
    if a == 1:
        actualizarUsuario()
    if a == 2:
        actualizarDireccion()
    else:
        print("opcion invalida, vuelve a intentarlo")
        mainActualizar()
        
'''def mainConsultar():
    print("¿Quiere listar todos los posibles resultados o solo locales?")
    print("1.- Todos")
    print("2.- Locales")
    a=int(input())
    if a == 1:
        mainConsultarTodo()
    if a == 2:
        mainConsultarLocal()
    else:
        print("opcion invalida, vuelve a intentarlo")
        mainConsultar() '''

def verificador(a,info):
    if a == 1:
        print("la direccion es ",info, "¿continuar?")
        print("1.- si")
        print("2.- cambiar")
        opcion=int(input())
        if opcion == 1:
            consultar(a,info)
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
'''def mainConsultarLocal():
    print("¿Con que dato desea consultar?")
    print("1.- Direcion")
    print("2.- RFC")
    print("3.- Nombre")
    a=int(input())
    if a == 1:
        print("Ingrese la direccion")
        direccion=input()
        verificador(a,direccion,2)
    if a == 2:
        print("Ingrese el RFC")
        rfc=input()
        verificador(a,rfc,2)
    if a == 3:
        print("Ingrese el Nombre")
        nombre=input()
        verificador(a,nombre,2)'''

def mainConsultarTodo():
    print("¿Con que dato desea consultar?")
    print("1.- Direcion")
    print("2.- RFC")
    print("3.- Nombre")
    a=int(input())
    if a == 1:
        print("Ingrese la direccion")
        direccion=input()
        verificador(a,direccion)
    if a == 2:
        print("Ingrese el RFC")
        rfc=input()
        verificador(a,rfc)
    if a == 3:
        print("Ingrese el Nombre")
        nombre=input()
        verificador(a,nombre)

def main():
    print("1.- Actualizar informacion")
    print("2.- Consultar informacion")
    print("3.- Crear Nuevo Registro")
    print("4.- Salir")
        
def menu():
    main()
    opcion=int(input("¿que desea hacer? "))
    if opcion == 1:
        mainActualizar()
    elif opcion == 2:
        mainConsultarTodo()
    elif opcion == 3:
        insertar()
    elif opcion == 4:
        exit()
    else:
        print("opcion invalida, vuelve a intentarlo")
          
menu()
