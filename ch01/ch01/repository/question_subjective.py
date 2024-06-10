from config.db import connect_db
from typing import Dict, Any

@connect_db
def insert_question_subjective(conn,qid:int,  item_id:int, correct_answer:str):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_subjective (qid, item_id, correct_answer) VALUES (%s, %s, %s)'
        values = (qid, item_id, correct_answer)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def update_question_subjective(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE question_subjective SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def delete_question_subjective(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM question_subjective WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_question_subjective(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_subjective'
        cur.execute(sql)
        quest_subjs = cur.fetchall()
        cur.close()
        return quest_subjs
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_question_subjective(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_subjective where id = {}'.format(id)
        cur.execute(sql)
        quest_subjs = cur.fetchall()
        answer = quest_subjs[0]
        cur.close()
        return answer
    except Exception as e:
        print(e)
    return None