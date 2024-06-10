from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_patient_contract(conn, pid:int, approved_by:str, approved_date:date, hcp:str, payment_mode:str, amount_paid:float, amount_due:float):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO patient_contract (pid, approved_by, approved_date, health_care_provider, payment_mode, amount_paid, amount_due) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = (pid, approved_by, approved_date, hcp, payment_mode, amount_paid, amount_due)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False  

@connect_db
def update_patient_contract(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE patient_contract SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def delete_patient_contract_id(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM patient_contract WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_patient_contract_pid(conn, pid:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM patient_contract WHERE pid = %s'
        values = (pid, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_patient_contract(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM patient_contract'
        cur.execute(sql)
        scores = cur.fetchall()
        cur.close()
        return scores
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_all_unpaid_patient(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM patient_contract where amount_due <> 0'
        cur.execute(sql)
        scores = cur.fetchall()
        cur.close()
        return scores
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_patient_contract(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM patient_contract where id = {}'.format(id)
        cur.execute(sql)
        scores = cur.fetchall()
        score = scores[0]
        cur.close()
        return score
    except Exception as e:
        print(e)
    return None