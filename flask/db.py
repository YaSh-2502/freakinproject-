import pymysql as p

def getconnection():    
    return p.connect(host="localhost",user="root",password="",database="carrental")

def selectrec(email):
    db=getconnection()
    cr=db.cursor()
    sql="select email,password from agent where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data

def selectrec1(email):
    db=getconnection()
    cr=db.cursor()
    sql="select CUST_EMAIL,CUST_PASSWORD from customer_details where CUST_EMAIL=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def insertc(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

def insertc1(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()


def inserto(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into car_owner values(%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

def insertcar(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into car_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

def insertp(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into payment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

def displaycar():
    db=getconnection()
    cr=db.cursor()
    sql="select * from car_details"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def displayp():
    db=getconnection()
    cr=db.cursor()
    sql="select * from payment"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def displaycp(e):
    db=getconnection()
    cr=db.cursor()
    sql="select * from payment where email=%s"
    cr.execute(sql,e)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data

def displayowner():
    db=getconnection()
    cr=db.cursor()
    sql="select * from car_owner"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def displaycust():
    db=getconnection()
    cr=db.cursor()
    sql="select * from customer_details"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def displayagent():
    db=getconnection()
    cr=db.cursor()
    sql="select * from agent"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def deleteo(OWNER_ID):
    db=getconnection()
    cr=db.cursor()
    sql="delete from car_owner where OWNER_ID=%s"
    cr.execute(sql,OWNER_ID)
    db.commit()
    db.close()

def deletec(CUST_ID):
    db=getconnection()
    cr=db.cursor()
    sql="delete from customer_details where CUST_ID=%s"
    cr.execute(sql,CUST_ID)
    db.commit()
    db.close()

def deletecar(CAR_ID):
    db=getconnection()
    cr=db.cursor()
    sql="delete from car_details where CAR_ID=%s"
    cr.execute(sql,CAR_ID)
    db.commit()
    db.close()

def deletep(CUST_NAME):
    db=getconnection()
    cr=db.cursor()
    sql="delete from payment where CUST_NAME=%s"
    cr.execute(sql,CUST_NAME)
    db.commit()
    db.close()

def selo(OWNER_ID):
    db=getconnection()
    cr=db.cursor()
    sql="select * from car_owner where OWNER_ID=%s"
    cr.execute(sql,OWNER_ID)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data[0]

def selc(CUST_ID):
    db=getconnection()
    cr=db.cursor()
    sql="select * from customer_details where CUST_ID=%s"
    cr.execute(sql,CUST_ID)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data[0]

def selcar(CAR_ID):
    db=getconnection()
    cr=db.cursor()
    sql="select * from car_details where CAR_ID=%s"
    cr.execute(sql,CAR_ID)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data[0]

def selp(CUST_NAME):
    db=getconnection()
    cr=db.cursor()
    sql="select * from payment where CUST_NAME=%s"
    cr.execute(sql,CUST_NAME)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data[0]


def updateo(t1):
    db=getconnection()
    cr=db.cursor()
    sql="update car_owner set OWNER_ID=%s,OWNER_NAME=%s,ADDRESS=%s,OWNER_CONTACT_NO=%s,OWNER_MAIL=%s,NO_OF_CAR_OWN=%s where OWNER_ID=%s"
    cr.execute(sql,t1)
    db.commit()
    db.close()

def updatec(t1):
    db=getconnection()
    cr=db.cursor()
    sql="update customer_details set CUST_ID=%s,CUST_FNAME=%s,CUST_LNAME=%s,LOCATION=%s,CUST_PHONE_NO=%s,CUST_EMAIL=%s,CUST_PASSWORD=%s,CUST_DRIVING_LICENSE_NO=%s,CUST_DL_EXPIRY_DATE=%s where CUST_ID=%s"
    cr.execute(sql,t1)
    db.commit()
    db.close()

def updatecar(t1):
    db=getconnection()
    cr=db.cursor()
    sql="update car_details set CAR_ID=%s,CAR_BRAND=%s,CAR_MODEL=%s,CAR_COLOR=%s,CAR_CAPACITY=%s,CAR_TYPE=%s,CAR_NO_PLATE=%s,OWNER_ID=%s,OWNER_NAME=%s,PAYMENT_AMOUNT=%s where CAR_ID=%s"
    cr.execute(sql,t1)
    db.commit()
    db.close()

def updatep(t1):
    db=getconnection()
    cr=db.cursor()
    sql="update payment set CUST_NAME=%s,CAR_NAME=%s,CAR_TYPE=%s,CUST_CONTACT_NO=%s,RENTAL_DATE=%s,RETURN_DATE=%s,PAYMENT_MODE=%s,PAYMENT_AMOUNT=%s where CUST_NAME=%s"
    cr.execute(sql,t1)
    db.commit()
    db.close()

def findamt(a,b):
    t=(a,b)
    db=getconnection()
    cr=db.cursor()
    sql="select  PAYMENT_AMOUNT from car_details where CAR_BRAND=%s and CAR_TYPE=%s"
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
