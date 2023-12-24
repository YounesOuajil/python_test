import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id integer Primary key,
            name text,
            age text,
            job  text,
            email text,
            gender text,
            mobile text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()


    def insert(self,name,age,job,email,gender,mobile,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
        (name,age,job,email,gender,mobile,address))
        self.con.commit()

    def fetch(self):
        self.cur.execute(" SELECT * from employees ")
        registr  = self.cur.fetchall()
        return registr    

    def remouve(self,id):
        self.cur.execute("delete  From employees where id=?",(id,))   
        self.con.commit()

    def update(self,id,name,age,job,email,gender,mobile,addresse):
        self.cur.execute("update employees set name=? , age=? , job=? , email=? , gender=?,mobile=?,address=? where id=?",
        (name,age,job,email,gender,mobile,addresse,id))
        self.con.commit()
        
    
    def ser(self,id):
        self.cur.execute(" SELECT * from employees  where id=?",(id,)) 
        registr  = self.cur.fetchall()
        return registr 
