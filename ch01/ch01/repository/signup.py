from config.db import connect_db
from typing import Dict, Any, List

@connect_db
def insert_signup(conn, user:str, passw:str, utype:str, fname:str, lname:str, cid:str) -> bool:
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO signup (username, password, user_type, firstname, lastname, cid) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (user, passw, utype, fname, lname, cid)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False
        

@connect_db
def update_signup(conn, id:int, details:Dict[str, Any]) -> bool:
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE signup SET {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_signup(conn, id) -> bool:
    try:
        cur = conn.cursor() 
        sql = 'DELETE FROM signup WHERE id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_signup(conn) -> List[Any]:
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM signup'
        cur.execute(sql)
        signups = cur.fetchall()
        cur.close()
        return signups
    except Exception as e:
        print(e)
    return None

@connect_db
def select_single_signup(conn, id:int) -> Any:
    try:
        cur = conn.cursor() 
        sql = 'SELECT * FROM signup where id = {}'.format(id)
        cur.execute(sql)
        signups = cur.fetchall()
        signup = signups[0]
        cur.close()
        return signup
    except Exception as e:
        print(e)
    return None
        
            
    
    
    
    