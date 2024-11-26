import cx_Oracle

# Database connection details
host = "localhost"
port = 1521
sid = "xe"
username = "system"
password = "welcome123"

# Creating a connection string
dsn = cx_Oracle.makedsn(host, port, sid)

# Establishing the connection
try:
	connection = cx_Oracle.connect(username, password, dsn)
	print("Connection successful!")
	
	#  creating a cursor to interact with the database
	cursor = connection.cursor()
	
	table_name=input("Enter the table name to create table:")
		
	cursor.execute(f"""create table {table_name} (emp_id number, firstName varchar (50), lastName varchar (50), designation varchar (50), dep varchar (50))""")
	n=int(input("Enter the number of rows that you want to insert:"))
	for i in range(1, n+1):
	  print(f"""Insert Row No:{i}""")
	  empID=int(input("Enter the employee id:"))
	  fN=input("Enter the first name:")
	  lN=input("Enter the lastname:")
	  des=input("Enter the designation:")
	  dep=input("Enter the department:")
	  cursor.execute( f"""insert into {table_name} values({empID},'{fN}','{lN}','{des}','{dep}')""")

	# Commit the transaction
	connection.commit()
	cursor.close()
	connection.close()
    
except cx_Oracle.DatabaseError as e:
    print(f"Error occurred: {e}")


Fetching Data from database:



Python code:

import cx_Oracles

# Database connection details
host = "localhost"
port = 1521
sid = "xe"
username = "system"
password = "welcome123"

# Creating a connection string
dsn = cx_Oracle.makedsn(host, port, sid)

# Establishing the connection
try:
	connection = cx_Oracle.connect(username, password, dsn)
	print("Connection successful!")
	
	#  creating a cursor to interact with the database
	cursor = connection.cursor()
	
	# Execute a query
	cursor.execute("SELECT  * FROM emp")
	
	# Fetch all rows
	rows = cursor.fetchall()
	
	# Process the data
	for row in rows:
	    print(row)	
	
	cursor.close()
	connection.close()
    
except cx_Oracle.DatabaseError as e:
    print(f"Error occurred: {e}")

