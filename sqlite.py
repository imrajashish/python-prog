#Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database.
import sqlite3
try:
   sqlite_Connection = sqlite3.connect('temp.db')
   conn = sqlite_Connection.cursor()
   print("\nDatabase created and connected to SQLite.")
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   record = conn.fetchall()
   print("\nSQLite Database Version is: ", record)
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("\nThe SQLite connection is closed.")

import  sqlite3
print("creating connecting ...")
conn  =  sqlite3.connect ('mydatabase.db' )
conn . close ()
print("\nThe SQLite connection is closed.")

#Write a Python program to create a SQLite database connection to a database that resides in the memory.
import sqlite3
try:
   sqlite_Connection = sqlite3.connect('temp.db')
   conn = sqlite3.connect(':memory:')
   print("\nMemory database created and connected to SQLite.")
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   print("\nSQLite Database Version is: ", sqlite3.version)
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("\nThe SQLite connection is closed.")

#Write a Python program to connect a database and create a SQLite table within the database.
import sqlite3
from sqlite3 import Error
def sql_connection():
   try:
     conn = sqlite3.connect('mydatabase.db')
     return conn
   except Error:
     print(Error)
def sql_table(conn):
   cursorObj = conn.cursor()
   cursorObj.execute("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
   print("\nagent_master file has created.")
   conn.commit()
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")

