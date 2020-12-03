# DDB_simulation
Simulating a distributed database.
 
Saul Armas y Javier Navarro    
Bases de Datos Distribuidas   
## Instrucciones para usar el simulador
### 1. Instalar algunas cosas que se necesitan, en Ubuntu20 (Linux) son:
#### MariaDB-server  ([referencia](https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04)) 
`sudo apt update`    
`sudo apt install mariadb-server`     
`sudo mysql_secure_installation`  <-- Elegir configuración deseada    
#### Conector python3 ([referencia](https://mariadb.com/kb/en/about-mariadb-connector-c/#installing-with-apt-get))
`sudo apt-get install libmariadb3`    
`sudo apt-get install libmariadb-dev`    
`pip3 install mariadb`     
#### Crear usuario ([referencia](https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04))
`sudo mariadb`    
`GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;`
`FLUSH PRIVILEGES;`
#### Tabulador PrettyTable
`pip3 install prettytable`    
### 2. Clonar el repositorio
Si no tienes git [instálalo](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) para poder correr clonar con la siguiénte línea:      
`git clone https://github.com/JavoJavo/DDB_simulation.git`    
### 3. Pon tus usuario y contraseña (los que creaste en mariadb) en el archivo de configuración (`config.json`)
Puedes dejar los otros campos como están.  
### 4. Crear las bases de datos simuladas con registros de ejemplo  
`python3 crearBases.py`   
Lo que hace la línea anterior es crear 2 bases de datos, una llamada Pátzcuaro y la otra llamada Morelia. Cada sucursal tiene 2 tablas, una llamada clientes y la otra llamada direcciones (la llaves están relacionadas). Cada tabla tiene 5 registros de ejemplo.
### 5. Haz transacciones de prueba
`python3 main2.py`

## Funcionalidades del simulador
1. Actualizar registros
2. Consultar registros
3. Insertar nuevos registros
4. Crear nuevas tablas

### Restricción para la creación de nuevas tablas
Las tablas nuevas que se creen forzosamente estarán conectadas únicamente a la tabla Clientes con 'IdCli'.




