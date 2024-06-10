from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_question_details(conn, id:int, cid:str, pid:int, exam_date:date, duration:int):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_details (id, cid, pid, exam_date, duration) VALUES (%s, %s, %s, %s, %s)'
        values = (id, cid, pid, exam_date, duration)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def update_question_details(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE question_details SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 


@connect_db
def delete_question_details(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM question_details WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_question_details(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_details'
        cur.execute(sql)
        quest_details = cur.fetchall()
        cur.close()
        return quest_details
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_question_details(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_details where id = {}'.format(id)
        cur.execute(sql)
        quest_details = cur.fetchall()
        detail = quest_details[0]
        cur.close()
        return detail
    except Exception as e:
        print(e)
    return None