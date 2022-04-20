import pymysql
import MarksheetBean
from MarksheetBean import *

class MarksheetDao():


    def add(self,mb):
        conn = pymysql.connect(host="localhost",user= "root",password="root",db = "marksheet",port= 3307)
        # crs=conn.cursor()
        with conn.cursor() as crs:
            query = "insert into mark values (%s, %s, %s, %s, %s)"
            data = mb.getName(), mb.getRollNo(), mb.getPhy(), mb.getChem(), mb.getMaths()
            crs.execute(query, args=data)
            conn.commit()
        conn.close()


    def update(self,mb):
        conn = pymysql.connect(host="localhost", user= "root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query= "update mark set name = %s, phy = %s, chem = %s, maths = %s where rollNo = %s"
            data = (mb.getName(), mb.getPhy() , mb.getMaths(),mb.getChem(), mb.getRollNo())
            crs.execute(query, args=data)
            conn.commit()
        crs.close()

    def delete(self,mb):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query= "delete from mark where rollNo = %s"
            data =  (mb.getRollNo())
            crs.execute(query, args=data)
            conn.commit()
        crs.close()

    # def select(self,mb):
    #     conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
    #     with conn.cursor() as crs:
    #         query= "select * from mark where rollNo = %s "
    #         data = (mb.getName(), mb.getPhy(), mb.getMaths(), mb.getChem(), mb.getRollNo())
    #         result = crs.fetchall()
    #         print("|| Name\t RollNo|t Phy\t Chem\t Maths")
    #         for row in result:
    #             print(row)
    #         crs.execute(query, args=data)
    #         conn.commit()
    #     crs.close()

    def search_single(self, mb):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            sql = "select * from mark where rollNo = %s"
            data = (mb.getRollNo())
            crs.execute(sql, args=data)
            result = crs.fetchall()
            conn.commit()
        crs.close()
        for d in result:
            print("|", d[0], "|", "\t", d[1], "|", "\t", d[2], "|", "\t", d[3], "|", "\t", d[4])

    def search_all(self):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            query = "select * from mark"
            crs.execute(query)
            result = crs.fetchall()
            conn.commit()
        crs.close()
        for d in result:
            print("|",d[0],"|","\t", d[1],"|","\t",d[2],"|","\t",d[3],"|","\t",d[4],"|",)

    def merit_list(self):
        conn = pymysql.connect(host="localhost", user="root", password="root", db="marksheet", port=3307)
        with conn.cursor() as crs:
            # query = "select rollNo,name,phe,chem,maths ,(phe +chem+maths) as total from where phe>=33 and chem>=33 and maths>=33 order by total desc limit 1; "
            query = "select  name,rollNo, phy, chem, maths, (phy+chem+maths) as total from mark where phy>=33 and chem>=33 and maths>=33 order by total desc limit 3 "
            crs.execute(query)
            result = crs.fetchall()
            conn.commit()
        conn.close()
        for d in result:
            print("|",d[0],"|","\t", d[1],"|","\t",d[2],"|","\t",d[3],"|","\t",d[4],"\t",d[5])
