# DDB_simulation
Simulating a distributed database.

## Avance
(Todavía nos faltan muchas cosas entre ellas el orden y la presentación)   
Saul Armas y Javier Navarro    
Bases de Datos Distribuidas   

### El primer paso es instalar 3 paquetes que se necesitan, que en este caso son:
MariaDB-server   
Mysql-python-connector    mariadb-python-connector -> pip3 install mariadb    
PrettyTable -> pip3 install prettytable    
Usamos Linux (Ubuntu20), ya para instalar los paquetes usamos las instrucciones que muestran en la documentación aquí. Y luego para instalar el conector corres el comando pip3 install mariadb.** pendiente     

### Pasos a seguir: 
Crear 1 base de datos que será el esquema de las sucursales que hay y las tablas que tiene cada una.
Crear las 2 bases de datos 2 tablas cada 1. Con 5 registros de prueba cada una.   
Bases de datos: una se llama Morelia y la otra se llama Pátzcuaro.   

	CREATE DATABASE Morelia;   
	CREATE DATABASE Pátzcuaro;   
	(Meterse a cada base de datos para crear las 2 tablas en cada una.)   
#### Tabla Direcciones:   
	CREATE TABLE Direcciones (   
	IdDir INT NOT NULL AUTO_INCREMENT,     
	calle VARCHAR(100),    
	numero VARCHAR(50),     
	colonia VARCHAR(100),    
	localidad VARCHAR(100),    
	estado VARCHAR(50),     
	CP CHAR(5),    
	PRIMARY KEY(IdDir)   
	)    

#### Tabla Clientes:   
	CREATE TABLE Clientes (   
	IdCli INT NOT NULL AUTO_INCREMENT,    
	Nombre VARCHAR(50),    
	ApellidoPaterno VARCHAR(50),     
	ApellidoMaterno VARCHAR(50),     
	RFC CHAR(13),     
	IdDir INT,    
	PRIMARY KEY (IdCli),    
	FOREIGN KEY (IdDir) REFERENCES Direcciones(IdDir)    
	)    
*** sólo va haber personas físicas (porque las personas morales tienen 12 caracteres en lugar de 13)?    
    
   
   
#### 20 ejemplos(5 por cada tabla):   
    
  
#### (BD Morelia)    
#### En tabla Direcciones:   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('San Benito', '556', 'Armando Madero','Morelia', 'Michoacán', '54954');    
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Cristobal Colón',  '84', 'Avante', 'Maravatío', 'Michoacán', '51682');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Leona Vicario',  '68B', 'Josefa Ortiz de Dominquez', 'Morelia', 'Michoacán', '56921');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Paseo de la República',  '599', 'Soledad', 'Morelia', 'Michoacán', '58088');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Villa Olímpica','775','Valladolid','Morelia','Michoacán','45444');     

#### En tabla Clientes:   
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Javier','Navarro','Espindola','VECJ880326001',1);    
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Armando','Villicaña','Gameza','VECJ880326801',4);   
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Karla','Herrera','Bilk','VECJ880326061',2);   
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Mario','Nuñez','Vizicalla','VECJ880326701',5);   
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Angela','Ornelas','Ceja','VECJ880326031',3);   




#### (BD Pátzcuaro)   
#### En tabla Direcciones:   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Batalla de Naco', '741', 'Juárez','Pátzcuaro', 'Michoacán', '54154');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('La otra banda',  '15', 'Roma', 'Pátzcuaro', 'Michoacán', '11681');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Piedra del Comal',  '11', 'Polanco', 'Pátzcuaro', 'Michoacán', '51121');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Balcón de los edecanes',  '48', 'Tlatelolco', 'Pátzcuaro', 'Michoacán', '58008');   
	INSERT INTO Direcciones (calle,  numero, colonia, localidad, estado, CP) VALUES ('Rayando el sol','747','Del Carmen','Pátzcuaro','Michoacán','45400');   



#### En tabla Clientes:   
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Hugo','Acosta','Acuña','VECS880326001',1);     
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Lucía','Aguilar','Aguirre','VECS880326801',2);     
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Daniel','Agustín','Ahumada','VECS880326061',3);    
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Martina','Alanis','Alarcón','VECS880326701',5);    
	INSERT INTO Clientes (Nombre,  ApellidoPaterno, ApellidoMaterno, RFC, IdDir) VALUES ('Alejandro','Alayón','Alcázar','VECS880326031',4);     

#### 1.2 Hacer base de datos donde se almacenen los nombres de las sucursales:     
	CREATE DATABASE sucursales;    
	CREATE TABLE nombres (n VARCHAR(100));     
	INSERT INTO nombres (n) VALUES ()     
	INSERT INTO nombres (n) VALUES ('Morelia'),('Pátzcuaro')    



### Crear un código en python con el conector que pueda hacer desde la terminal:   
Insertar nuevos clientes (en la base de datos local)      
Actualizar    
Buscar (deben poderse mostrar todos los clientes) (buscar de todas las sucursales al mismo tiempo)    
Insertar tabla:      
La constraint que se me ocurre para que sea mucho más fácil y organizado es que las nuevas tablas estén obligadas a estar conectadas a la tabla 'Clientes' y únicamente a esa. Es decir la llave foránea de las nuevas tablas agregadas será siempre el id de 'Clientes'.

### Crear función 
