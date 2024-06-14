from couchbase.options import ClusterOptions, QueryOptions
from couchbase.n1ql import N1QLQuery
from modules import cb
from typing import Any, List, Dict

class DirectMessageRepository:
    def __init__(self):
        pass
    
    def insert_dm(self, details:Dict[str, Any]):
        try:
            cb_coll = cb.scope("tfs").collection("direct_messages") 
            key = "chat_" + str(details['id']) + '-' + str(details["date_sent"])
            cb_coll.insert(key, details)
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_dm(self, details:Dict[str, Any]):
        try:
            cb_coll = cb.scope("tfs").collection("direct_messages") 
            key = "chat_" + str(details['id']) + '-' + str(details["date_sent"])
            cb_coll.upsert(key, details)
            return True
        except Exception as e:
            print(e)
        return False 
    
    def delete_dm_key(self, details:Dict[str, Any]):
        try:
            cb_coll = cb.scope("tfs").collection("direct_messages") 
            key = "chat_" + str(details['id']) + '-' + str(details["date_sent"])
            cb_coll.remove(key)
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete_dm_sender(self, sender):
        try:
            cb_scope = cb.scope("tfs")
            stmt = f"delete from `direct_messages` where `sender_id` LIKE '{sender}'"
            cb_scope.query(stmt)
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete_dm_id(self, id):
        try:
            cb_scope = cb.scope("tfs")
            stmt = f"delete from `direct_messages` where `id` = {id}"
            cb_scope.query(stmt)
            return True
        except Exception as e:
            print(e)
        return False  
    
    def select_dm(self, key):
        cb_coll = cb.scope("tfs").collection("direct_messages") 
        record = cb_coll.get(key)
        return record
    
    def select_all_dm(self):
        cb_scope = cb.scope("tfs")
        raw_data = cb_scope.query('select * from `direct_messages`', QueryOptions(read_only=True))
        records = [rec for rec in raw_data.rows()]
        return records
    
    def select_dm_sender(self, sender):
        cb_coll = cb.scope("tfs")
        raw_data = cb_coll.query(f"select * from `direct_messages` where `sender_id` LIKE '{sender}'", QueryOptions(read_only=True))
        records = [rec for rec in raw_data.rows()]
        return records