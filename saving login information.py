import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

username=input('enter your email: ')

if re.fullmatch(regex, username):
    pass
else:
    while re.fullmatch(regex, username)==None:
        username=input('the username format should be expression@string.string. please enter your email again: ')
        
password=input('enter your password: ')      


import mysql.connector 
cnx = mysql.connector.connect(
user='root', password='1234', host='127.0.0.1', database='test'
)
cursor = cnx.cursor()
cursor.execute('INSERT INTO emails VALUES(\'%s\',\'%s\')'%(username,password)) 
cnx.commit()
cnx.close()