import mysql.connector

dbUser="root"
dbPass=""
dbHost="127.0.0.1"
dbName="demodb"

class Database(object):
    @staticmethod
    def getConnection():
        return mysql.connector.connect(user=dbUser,password=dbPass,host=dbHost,database=dbName)
    @staticmethod
    def escape(value):
        return value.replace("'","''")
    @staticmethod
    def getResult(query,getOne=False):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        if getOne:
            result_set = cur.fetchone()
        else:
            result_set = cur.fetchall()
        cur.close()
        conn.close()
        return result_set
    @staticmethod
    def doQuery(query):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        lastId = cur.lastrowid
        cur.close()
        conn.close()
        return lastId

class Employee(object):
    def __init__(self,id=0):
        self.firstname=""
        self.lastname=""
        self.employeenumber=0
        self.email=""
        self.phone= ""

        if(not type(id)==int):
            id=int(id)
        query = "SELECT id,firstname,lastname, employeenumber,email,phone FROM employee where id=%d " %  id
        result_set = Database.getResult(query,True)
        self.id=id
        if not result_set is None:
            self.id = result_set[0]
            self.firstname=result_set[1]
            self.lastname=result_set[2]
            self.employeenumber=result_set[3]
            self.email=result_set[4]
            self.phone=result_set[5]
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = "insert into employee (firstname, lastname, employeenumber, email, phone) values ('%s','%s','%s','%s','%s','%s')"% (Database.escape(self.firstname), Database.escape(self.lastname), self.employeenumber,self.email,self.phone)
        self.id=Database.doQuery(query)
        return self.id
    def update(self):
        query = "update employee set firstname='%s', lastname='%s', employeenumber='%s', email='%s', phone='%s' where id=%d"% (Database.escape(self.firstname), Database.escape(self.lastname), self.employeenumber,self.email,self.phone,self.id)
        # query = ("delete from page where id=%s" % id)
        return Database.doQuery(query)
Employee()
# class Address(object):
#
# class Income(object):
