from config.db import connect_db
from typing import Dict, Any

@connect_db
def insert_patient_score(conn, pid:int, qid:int, score:float, total:float, status:str, percentage:float):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO patient_score (pid, qid, score, total, status, percentage) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (pid, qid, score, total, status, percentage)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False  

@connect_db
def update_patient_score(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE patient_score SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def delete_patient_score(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM patient_score WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_patient_score(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM patient_score'
        cur.execute(sql)
        scores = cur.fetchall()
        cur.close()
        return scores
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_patient_score(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM patient_score where id = {}'.format(id)
        cur.execute(sql)
        scores = cur.fetchall()
        score = scores[0]
        cur.close()
        return score
    except Exception as e:
        print(e)
    return None