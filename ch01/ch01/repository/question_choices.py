from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_question_choice(conn, qid:int, item_id:int, choice:str, choice_text:str, correct_choice:bool):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_choices (qid, item_id, choice, choice_text, correct_choice) VALUES (%s, %s, %s, %s, %s)'
        values = (qid, item_id, choice, choice_text, correct_choice)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def update_question_choice(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE question_choices SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def delete_question_choice(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM question_choices WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_question_choice(conn):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_choices'
        cur.execute(sql)
        quest_choices = cur.fetchall()
        cur.close()
        return quest_choices
    except Exception as e:
        print(e)
    return None 

@connect_db
def select_single_question_choice(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM question_choices where id = {}'.format(id)
        cur.execute(sql)
        quest_choices = cur.fetchall()
        choice = quest_choices[0]
        cur.close()
        return choice
    except Exception as e:
        print(e)
    return None