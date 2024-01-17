import sqlite3

#connect to SQlite
connection = sqlite3.connect("student.db")

#create a cursor object to insert records, create table
cursor=connection.cursor()

#create table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""
cursor.execute(table_info)

#insert records
cursor.execute('''Insert into STUDENT values('Krish', 'Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Sudhanshu', 'Data Science','B')''')
cursor.execute('''Insert into STUDENT values('Amulya', 'Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Aditya', 'Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Vikas', 'DEVOPS','A')''')
cursor.execute('''Insert into STUDENT values('Dipesh', 'DEVOPS','A')''')

#Display all records
print("The inserted records are")
data=cursor.execute("select * from STUDENT")
for row in data:
    print(row)

#commit changes
connection.commit()
connection.close()