


import pymysql
conn = pymysql.connect(host='localhost' ,user='root',password='',db='restrauntdb2022')
a=conn.cursor()
"""
create table

q = " create table Foodinfo(dno int ,dname  varchar(100),dprice  float)"
a.execute(q)


#extracting data from table

s= "insert into Foodinfo (dno,dname,dprice)values(%s , %s ,%s)"
Foodinfos = [ (2,'pav bhaji',150),(3,'chole samose',80),(4,'aloo tikki',50),(5,'masala dosa',170)]
a.executemany(s,Foodinfos)
conn.commit()

s= " select *from Foodinfo"
a.execute(s)
result=a.fetchall()
for rec in result:
    print(rec)

## update table record

s= "update foodinfo set dprice=dprice+10 where dprice>100"
a.execute(s)
conn.commit()

##delete table from record

s= " delete from foodinfo where dno=5"
a.execute(s)
conn.commit()



s= "insert into Foodinfo (dno,dname,dprice)values(%s , %s ,%s)"
Foodinfos = [ (5,'kaju katli',500),(6,'malai barfi',600),(7,'gulab jamun',100),(8,'rasmalai',175)]
a.executemany(s,Foodinfos)
conn.commit()

"""


t=True
while t:
    print("Main Menu")
    print("1. Create Table 2. Insert 3. Display 4. Search 5. Update 6. Delete 7. Exit")
    op=int(input("Enter Your Choice: "))
    if op==1:
        tname=input("Enter Table Name: ")
        #q="create table abc(dno int primary key,dname varchar(50),dprice float)"
        q="create table "+tname+"(dno int primary key,dname varchar(50),dprice float)"
        a.execute(q)
        print("Table Created...")
 
    elif op==2:
        no = int(input("Enter Dish no:"))
        name=input("Enter Dish name:")
        price=float(input("Enter Dish price:"))

        q="insert into Foodinfo values("+str(no) +",'"+name+"',"+str(price)+")"        
        a.execute(q)
        print("Record inserted")
        conn.commit()
        
        
        
    elif op==3:
        a.execute("select * from Foodinfo")
        data=a.fetchall()
        print(data)
        for d in data:
            print(d)
    
        
    elif op==4:
        print("Select Option\n1. Search by Dish no: 2. Search by Dish name: 3. Search by Price 4. None")
        op=int(input("Enter Your Choice: "))
        if op==1:
            rol=int(input("Search by Dish no: "))
            q="select*from Foodinfo where dno="+str(rol)
            a.execute(q)
            data=a.fetchall()
            print(data)
         
        elif op==2:
             name=input("Searched by Dish Name: ")
             q="select*from book where dname='"+name+"'"
             a.execute(q)
             data=a.fetchall()
             print(data)
          
        elif op==3:
             bprice=float(input("Enter Dish price: "))
             q="select * from book where dprice="+str(bprice)
             a.execute(q)
             data=a.fetchall()
             print(data)

        elif op==4:
            print("No Change...")
        else:
            print("Invalid input...")
      
    elif op==5:
          rol=int(input("Enter Dish price: "))
          q="select * from Foodinfo where dname="+str(rol)
          a.execute(q)
          data=a.fetchall();
          print(data)
          print("Main Menu\n1. DishNo 2. DishName 3. Both 4. None")
          op=int(input("Enter Your Choice: "))
          
          if op==1:
              no=int(input("Enter DishNO: "))
              q="update Foodinfo set dno='"+str(no)+"' where dprice="+str(rol)
              a.execute(q)
              print(str(no)+" Updated for "+str(rol))
          

          elif op==2:
              name=input("Enter DishName: ")
              q="update Foodinfo set dname='"+name+"' where dprice="+str(rol)
              a.execute(q)
              print(name+" Updated for "+str(rol))
             
          elif op==3:
              no=int(input("Enter DishNO: "))
              name=input("Enter DishName: ")
              q="update Foodinfo set dname='"+name+"', dno="+str(no)+" where dprice="+str(rol)
              a.execute(q)
              print(name+" and "+str(no)+" Updated for "+str(rol))
          elif op==4:
              print("No Change...")
          else:
              print("Invalid input...")
              conn.commit()

    elif op==6:
        rol = int(input("Enter Dish price:"))
        q="delete from Foodinfo where dprice="+str(rol)
        a.execute(q)
        conn.commit()
        print("Record Deleted...")
            
    else:
        print("Invalid Input...")
    ch=int(input("Do you want to cont. 1. Yes 2. No"))
    if ch!=1:
          t=False
   

