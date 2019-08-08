import pyodbc

# set up some constants
MDB = 'emple_depart.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
conn = con.cursor()

# run a query and get the results 
SQL = 'SELECT * FROM emple;'
rows = conn.execute(SQL).fetchall()

print(rows)

conn.close()
con.close()