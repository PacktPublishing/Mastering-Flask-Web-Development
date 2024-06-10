from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_question_pool(conn, qid:int, question:str, type:int):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_pool (qid, question, type) VALUES (%s, %s, %s)'
        values = (qid, question, type)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def update_question_pool(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE question_pool SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def delete_question_pool(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM question_pool WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_question_pool(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_pool'
        cur.execute(sql)
        quest_pools = cur.fetchall()
        cur.close()
        return quest_pools
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_question_pool(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_pool where id = {}'.format(id)
        cur.execute(sql)
        quest_pools = cur.fetchall()
        question = quest_pools[0]
        cur.close()
        return question
    except Exception as e:
        print(e)
    return None

@connect_db
def get_current_id(conn):
    try:
        cur = conn.cursor() 
        sql = "SELECT id from question_pool order by id DESC limit 1"
        cur.execute(sql)
        curr_id = cur.fetchall()
        cur.close()
        return curr_id
    except Exception as e:
        print(e)
    return None  