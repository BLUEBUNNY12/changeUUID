import mysql.connector
import os
import random

cnx = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx2 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx3 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx4 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')



cursor = cnx.cursor()
cursor2 = cnx2.cursor()
cursor3 = cnx3.cursor()
cursor4 = cnx4.cursor()


def mainMenu():

    print ("""
    1. Enter a specific UUID, like 09DEFB00-FB89-4EFC-B0D1-5429E6083896, to change its info
    2. Change info on a random UUID
    3. Exit/Quit
    """)
    number = input("What would you like to do?")
    if number == "1":
        selectMenu()
    elif number == "2":
        randomMenu()
    elif number == "3":
        print("\nGoodbye")
    elif number != "":
        print("\nNot a valid choice. Try again.")
        mainMenu()


def selectMenu():

    UUID = input("Enter UUID: ")
    FIRST_NM = input("Enter a new first name: ")
    LAST_NM = input("Enter a new last name: ")
    STREET = input("Enter your street name: ")

    print("You entered '%s' '%s' '%s'" % (FIRST_NM, LAST_NM, STREET))


    cursor2.execute("""UPDATE dBAngelaSchneider.NAMES SET
      FIRST_NM = '%s',
      LAST_NM = '%s'
      WHERE UUID = '%s'""" % (FIRST_NM, LAST_NM, UUID))
    cnx2.commit()

    cursor3.execute("""UPDATE dBAngelaSchneider.ADDRESSES SET
    STREET = '%s'
    WHERE UUID = '%s'""" % (STREET, UUID))
    cnx3.commit()

    print("UUID '%s' is updated" % (UUID))



def randomMenu():

    FIRST_NM = input("Enter a new first name: ")
    LAST_NM = input("Enter a new last name: ")
    STREET = input("Enter your street name: ")

    print("You entered '%s' '%s' '%s'," % (FIRST_NM, LAST_NM, STREET))

    SELECT * FROM dBAngelaSchneider.UUIDS
    ORDER BY RAND()
     LIMIT 1


    cursor.execute("""UPDATE dBAngelaSchneider.NAMES SET
      FIRST_NM = '%s',
      LAST_NM = '%s'
      WHERE UUID =
     """ % (FIRST_NM, LAST_NM))
    cnx.commit()

    cursor4.execute("""UPDATE dBAngelaSchneider.ADDRESSES SET
    STREET = '%s'
    WHERE UUID = RAND()
    ORDER BY RAND()
    LIMIT 1""" % (STREET))
    cnx4.commit()

    print("Random UUID is updated")

mainMenu()




cursor.close()
cnx.close()

cursor2.close()
cnx2.close()

cursor3.close()
cnx3.close()

cursor4.close()
cnx4.close()
