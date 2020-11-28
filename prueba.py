import mariadb
'''
def select_contacts(cur):
   """Retrieves the list of contacts from the database"""

   # Retrieve Contacts
   cur.execute(" SELECT IdCli FROM Clientes ORDER BY IdCli DESC LIMIT 1")
   

   
   # Get field info from cursor
def get_field_info(cur):
   """Retrieves the field info associated with a cursor"""

   field_info = mariadb.fieldinfo()

   field_info_text = []

   # Retrieve Column Information
   for column in cur.description:
      column_name = column[0]
      column_type = field_info.type(column)
      column_flags = field_info.flag(column)

      field_info_text.append(f"{column_name}: {column_type} {column_flags}")

   return field_info_text

   
   

try:
   conn = mariadb.connect(
         user="javo",
         password="b",
         host="localhost",
         database="prueba")

   cur = conn.cursor()

   select_contacts(cur)

   field_info_text = get_field_info(cur)

   print("Columns in query results:")

   print("\n".join(field_info_text))

   conn.close()

except Exception as e:
   print(f"Error: {e}")
'''

   
def print_contacts(cur):
   """Retrieves the list of contacts from the database and prints to stdout"""

   # Initialize Variables
   contacts = []

   # Retrieve Contacts
   cur.execute(" SELECT IdCli FROM Clientes ORDER BY IdCli DESC LIMIT 1")

   # Prepare Contacts
   for (IdCli) in cur:
      contacts.append(f"{IdCli}")

   # List Contacts
   print("\n".join(contacts))
   
try:
   conn = mariadb.connect(
         user="javo",
         password="b",
         host="localhost",
         database="prueba")

   cur = conn.cursor()
except Exception as e:
   print(f"Error: {e}")
   
print_contacts(cur)
