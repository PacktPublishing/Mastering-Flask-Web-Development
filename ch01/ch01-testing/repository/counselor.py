from config.db import connect_db
from typing import Dict, Any, List
from datetime import date

@connect_db
def insert_counselor(conn, id:int, cid:str, fname:str, lname:str, age:int, position:str, prof_started:date):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO counselor (id, cid, firstname, lastname, age, position, profession_started) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = (id, cid, fname, lname, age, position, prof_started)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def update_counselor(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE counselor SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False   

@connect_db
def delete_counselor(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM counselor WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False


@connect_db
def select_all_counselor(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM counselor'
        cur.execute(sql)
        counselors = cur.fetchall()
        cur.close()
        return counselors
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_counselor(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM counselor where id = {}'.format(id)
        cur.execute(sql)
        counselors = cur.fetchall()
        counselor = counselors[0]
        cur.close()
        return counselor
    except Exception as e:
        print(e)
    return None