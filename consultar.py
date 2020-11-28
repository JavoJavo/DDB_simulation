import mariadb 
#pip3 install prettytable
from prettytable import PrettyTable

## SOLO SIRVE PARA RELACIONES UNO A UNO,(NO SIRVE PARA RELACIONES UNO A MUCHOS O MUCHOS A MUCHOS)


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
    
'''
atributo = input('Dame atributo:')
valor = input('Dame valor: ')
Consultar_clientes(atributo, valor)
'''
Consultar_clientes('Localidad','Pátzcuaro')
