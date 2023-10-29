# import pandas as pd
# import mysql.connector as sql
# conn = sql.connect(host='new connection', user='root', passwd='Omkar123@#', database='stationary_system')
# if conn.is_connected():
#     print('Successfully Connected')
#
#
#
#
#
# def menu():
#
#     print()
#     print("********************************************")
#     print("STATIONERY STORE MANAGEMENT SYSTEM")
#     print("********************************************")
#     print()
#     print ()
#     print("1. About the project")
#     print("2. Display all products available in stock")
#     print("3. Display all stationery items in alphabetical order")
#     print("4. Add new purchased purchased in stock table")
#     print("5. Update price of a stationery")
#     print("6. Delete a stationery detail from the table stock of not available")
#     print("7. Accept customer order and show bill")
#     print("8. Show details of sales done from table bill")
#     print("9. Enter all customers orders and maintain record")
#     print("10. Total Bill to be paid - customer wise")
#
#     print("12. Total stationery bought and price of each according to Mobile number")
#     print("************************************************")
#
#
#
#
#
#
#
#
#
#
#
#
# menu()
#
# #
# #
# #
# # def about ():
# #     print(“You are welcome to STATIONERY STORE MANAGEMENT PROJECT. It has 12 choices. It has used 2 tables named as customer and inventory”)
# #
# #
# #
# # def showlist():
# #     print(“Display all details of stationery items available.”)
# #     print()
# #     df= pd.read_sql ("select * from INVENTORY", conn)
# #     print(df)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def sortstationery():
# #     print(“Sorting stationery product in ascending order”)
# #     print()
# #     df=pd.read_sql ("select * from INVENTORY",conn)
# #     df=df.sort_values('ITEMNAME')
# #     print(df)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def addstock():
# #     c1 = conn.cursor()
# #     print("Stationery already is stock")
# #     print()
# #     df=pd.read_sql ("select * from INVENTORY",conn)
# #     print(df)
# #
# #
# #
# #
# #     L = []
# #     ITEMNAME = input ("Enter Stationery Name :")
# #     L.append (ITEMNAME)
# #     QUANTITY = input ("Enter Quantity of Stationery Item :")
# #     L.append (QUANTITY)
# #     PURCHASEDPRICE = input ("Enter Price :")
# #     L.append (PURCHASEDPRICE)
# #     TRADERSNAME = input (“Enter Trader’s Name :”)
# #     L.append (TRADERSNAME)
# #     INVENTORY = (L)
# #     sql="insert into INVENTORY (ITEMNAME, QUANTITY, PURCHASEDPRICE, TRADERSNAME) values (%s,%s,%s,%s)
# #
# #
# #
# #
# #     c1.execute (sql, INVENTORY)
# #     conn.commit ()
# #     print (“Record Inserted”)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def updatestock():
# #     print (“Change Price of Stationery Item”)
# #     c1 = conn.cursor()
# #     print ("Old Prices")
# #     df = pd.read_sql ("select * from INVENTORY", conn)
# #     print(df)
# #     c1.execute ("update INVENTORY set PURCHASEDPRICE = PURCHASEDPRICE +30 where ITEMNAME='SHARPNERS' ")
# #     print ("Price increased")
# #     print ()
# #     #conn.commit()
# #     df = pd.read_sql ("select * from INVENTORY", conn)
# #     print (df)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def deletestock():
# #     print (“Before any changes in INVENTORY”)
# #     print ()
# #     df = pd.read_sql ("select * from INVENTORY",conn)
# #     print(df)
# #     print()
# #     mc = conn.cursor()
# #     mc.execute ("delete from INVENTORY where PURCHASEDPRICE = 'SHARPNERS'", conn)
# #     print ("Record deleted")
# #     df = pd.read_sql ("select * from INVENTORY", conn)
# #     print (df)
# #     #conn.commit()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# def custorder():
#     print("Stationery name and price of each stationary is shown below")
#     print()
#     df=pd.read_sql ("select * from INVENTORY", conn)
#     print (df)
#     print ()
#     print ()
#     print ()
#     print ()
#     print ()
#     x = int (input (“Enter your ITEMNAME please :”))
#     n = int (input (“How much quantity do you want to buy ? :”))
#
#
# #
# #
# #     if (x == ‘BOOKCOVERS’) :
# #        print ()
# #        print (“You have brought Book covers.”)
# #        print ()
# #        print (“Price is Rs.30 each.”)
# #        s = 30*n
# # elif (x == ‘DRAWINGBOOK’) :
# #        print ()
# #        print (“You have brought Drawing book.”)
# #        print ()
# #        print (“Price is Rs.60 each.”)
# #        s = 60*n
# # elif (x == ‘ERASERS’) :
# #        print ()
# #        print (“You have brought Erasers.”)
# #        print ()
# #        print (“Price is Rs.3 each.”)
# #        s = 3*n
# # elif (x == ‘NOTEBOOK’) :
# #        print ()
# #        print (“You have brought Notebook.”)
# #        print ()
# #        print (“Price is Rs.60 each.”)
# #        s = 60*n
# # elif (x == ‘PAPERSHEETS’) :
# #        print ()
# #        print (“You have brought Paper Sheets.”)
# #        print ()
# #        print (“Price is Rs.30 each.”)
# #        s = 30*n
# # elif (x == ‘PENCILS’) :
# #        print ()
# #        print (“You have brought Pencils.”)
# #        print ()
# #        print (“Price is Rs.5 each.”)
# #        s = 5*n
# # elif (x == ‘PENS’) :
# #        print ()
# #        print (“You have brought Pens.”)
# #        print ()
# #        print (“Price is Rs.10 each.”)
# #        s = 10*n
# # elif (x == ‘POUCHES’) :
# #        print ()
# #        print (“You have brought Pouches.”)
# #        print ()
# #        print (“Price is Rs.50 each.”)
# #        s = 50*n
# # elif (x == ‘SCALES’) :
# #        print ()
# #        print (“You have brought Scales.”)
# #        print ()
# #        print (“Price is Rs.10 each.”)
# #        s = 10*n
# # elif (x == ‘SHARPNERS’) :
# #        print ()
# #        print (“You have brought Sharpners.”)
# #        print ()
# #        print (“Price is Rs.3 each.”)
# #        s = 3*n
# # else :
# #        print (“Please Enter correct ITEMNAME.”)
# # print (“YOUR BILL AMOUNT IS = Rs.”, s, “/n”)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def billrecords () :
# #      print (“Display Contact No. of Customers and Stationery items and its Quantity and Price.”)
# #      print ()
# #      df = pd.read_sql (“select * from CUSTOMER”, conn)
# #      print (df)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def recordorder () :
# #      print (“List and Price of Stationery Items.”)
# #      print ()
# #      df = pd.read_sql (“select * from INVENTORY”, conn)
# #      print (df)
# #      print ()
# #      print (‘Insert into bill records new sale’)
# #      mc = conn.cursor ()
# #
# #
# #
# #
# #      L = []
# #     customer_id = input (“Enter Phone No. :”)
# #     L.append(customer_id)
# #     ITEMNAME = input ("Enter Stationery Item Name :")
# #     L.append(ITEMNAME)
# #     PURCHASEDPRICE = input ("Enter Price :")
# #     L.append(PURCHASEDPRICE)
# #     TRADERSNAME = input (“Enter Trader’s Name :”)
# #     L.append(TRADERSNAME)
# #
# #
# #
# #
# #     CUSTOMER_REC = (L)
# #     sql = “insert into CUSTOMER (customer_id, phone_no, items, amount, email_id, customer_name) values (%s, %s, %s, %s)
# #     mc.execute (sql, CUSTOMER_REC)
# #     conn.commit ()
# #     print (“Record Inserted”)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# def sumbillbycust () :
#     df  = pd.read_sql (“select * from CUSTOMER”, conn)
#     print (df)
#     print (“Total money spent on various Stationery Items by a customer.”)
#
#
#
#
#     m = float (input (“Phone No. :”))
#     print (“Your Order.”)
#     print ()
#     print ()
#     qry = “select NAME, TOTAL_PURCHASE_AMT from CUSTOMER where PHONE_NO = %s;” %(m,)
#     df = pd.read_sql (qry, conn)
#     print (df)
#
#
#
#
#     qry1 = “select QUANTITY*PRICE as ‘Total Cost of Each Item’ from CUSTOMER where PHONE_NO = %s;” %(m,)
#     df = pd.read_sql (qry1, conn)
#     print (df)
#     print ()
#     print ()
#
#
#
#
#     qry2 = “select TOTAL_PURCHASE_AMT from CUSTOMER where PHONE_NO = %s;” %(m,)
#     df = pd.read_sql (qry2, conn)
#     print (df)
#
#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # def searchbyphone () :
# #     df = pd.read_sql (“select * from CUSTOMER”, conn)
# #     print (df)
# #     print ()
# #     print (“Enter your Phone no. to find all the details of your purchasing.”)
# #     m = float (input (“Phone No. :”))
# #     qry “select NAME, TOTAL_PURCHASE_AMT from CUSTOMER where PHONE_NO = %s;” %(m,)
# #     df = pd.read_sql (qry, conn)
# #     print (df)
# #     # for x in mc :
# #     # print (x)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # opt = “”
# # opt = int (input (“Enter Your Choice :”))
# #
# #
# #
# #
# # if opt == 1 :
# #    about ()
# # elif opt == 2 :
# #    showlist ()
# # elif opt == 3 :
# #    sortstationery ()
# # elif opt == 4 :
# #    addstock ()
# # elif opt == 5 :
# #    updatestock ()
# # elif opt == 6 :
# #    deletestock ()
# # elif opt == 7 :
# #    custorder ()
# # elif opt == 8 :
# #    billrecords ()
# # elif opt == 9 :
# #    recordorder ()
# # elif opt == 10 :
# #    sumbillbycust ()
# # elif opt == 12 :
# #    searchbyphone ()
# # else :
# #     print (“Invalid Option.”)
# #
# #
# #
# #
# #
# #
# #
# #
# # import winsound
# winsound.Beep (1000, 300)
print(299 + 30 +500+25+100+159+212+48+220+81)