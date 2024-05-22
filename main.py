################ # task 1

# import sqlite3

# connection=sqlite3.connect("products.db")
# cursor=connection.cursor()


# def create_Table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCT (name TEXT, price INT, sales INT)")
#     connection.commit()

# def add_data(name,price,sales):
#     cursor.execute("INSERT INTO PRODUCT VALUES (?,?,?)",(name,price,sales))
#     connection.commit()
# #add_data("notebook",1500,5)
# #add_data("klaveye",150,6)
# #add_data("mous",10,17)   
# #add_data("monitor",180,7)
# # create_Table()
# def qazanc():
#     cursor.execute("SELECT NAME,PRICE*SALES AS QAZANC FROM PRODUCT")
#     data=cursor.fetchall()
#     for i in data:
#         print(i)

# qazanc()
# # add_data("monitor",180,7)

# connection.close()

############################task2



# import sqlite3
# connection=sqlite3.connect("database.db")
# cursor=connection.cursor()

# def create_Table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS WORKERS ( name TEXT, salary INT, department TEXT)")
#     connection.commit()

# def add_data(name,salary,department):
#     cursor.execute("INSERT INTO WORKERS VALUES (?,?,?)",(name,salary,department))
#     connection.commit()    
# #add_data("emin",5000,"IT")
# # add_data("kenan",3000,"IT")
# # add_data("veli",200,"Temir")
# # add_data("sahil",700,"satis")
# # add_data("sebine",1700,"satis")

# def sorgu():
#     cursor.execute("SELECT SALARY FROM WORKERS WHERE DEPARTMENT=? AND salary > ? ORDER BY SALARY DESC",("satis",600) )
#     data=cursor.fetchall()
#     print(data)

# sorgu()

# create_Table()


######################task3



# import sqlite3
# connection=sqlite3.connect("database.db")
# cursor=connection.cursor()
# def create_Table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS BOOKS ( ad TEXT, janr INT, nesrili INT)")
#     connection.commit()


# #create_Table()
# def add_data(ad,janr,nesrili):
#     cursor.execute("INSERT INTO BOOKS VALUES (?,?,?)",(ad,janr,nesrili))
#     connection.commit() 

# # add_data("kitab1","drama",2014)
# # add_data("kitab2","tragedy",2016)
# # add_data("kitab3","detektiv",2012)
# # add_data("kitab4","fantastik",2017)
# # add_data("kitab5","detektiv",2019)
# def sorgu():
#     cursor.execute("SELECT * FROM BOOKS WHERE nesrili>? order by janr",(2015,))
#     data=cursor.fetchall()
#     print(data)
# sorgu()
#connection.close()


#########################task4


# import sqlite3
# connection=sqlite3.connect("database2.db")
# cursor=connection.cursor()
# def create_Table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS FILMS ( ad TEXT, CIXIS INT, RAITING INT)")
#     connection.commit()

# create_Table()
# def add_data(ad,cixis,raiting):
#     cursor.execute("INSERT INTO FILMS VALUES (?,?,?)",(ad,cixis,raiting))
#     connection.commit() 

# # add_data("candostum",2015,9)
# # add_data("fightclub",2008,8)
# # add_data("aslapesetme",2013,10)
# # add_data("merhaba",2024,9)
# # add_data("ali",2012,7)
# # add_data("alim",1990,7)
# # add_data("alii",1995,6)

# def sorgu1():
#     cursor.execute("select * from films where cixis<? order by cixis",(2000,))
#     data=cursor.fetchall()
#     print(data)


# def sorgu1():
#     cursor.execute("select * from films where cixis<? order by cixis",(2000,))
#     data=cursor.fetchall()
#     print(data)

# def sorgu2():
#     cursor.execute("select * from films where RAITING>? order by RAITING DESC",(7,))
#     data=cursor.fetchall()
#     print(data)

# sorgu2()
# connection.close()    