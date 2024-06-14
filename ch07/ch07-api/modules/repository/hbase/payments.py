from typing import Dict, List, Any
from happybase import Table
 
class PaymentRepository:
    
    def __init__(self, pool):
        self.pool = pool
    
    def upsert_details(self, rowkey, tutor_id, stud_id, ccode, fee) -> bool:
        record = {'details:id' : str(rowkey), 'details:tutor_id': tutor_id, 'details:stud_id': stud_id, 'details:course_code': ccode, 'details:total_package': str(fee)}
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                tbl.put(row=str(rowkey).encode('utf-8'), data=record)
            return True
        except Exception as e:
            print(e)
        return False
    
    def upsert_payment(self, rowkey, receipt_id, amount) -> bool:
        record = {'items:id' : str(rowkey),'items:receipt_id': receipt_id, 'items:amount': str(amount)}
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                tbl.put(str(rowkey).encode('utf-8'), data=record)
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete_record(self, rowkey) -> bool:
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                tbl.delete(rowkey.encode('utf-8'))
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete_payment_details(self, rowkey) -> bool:
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                tbl.delete(rowkey.encode('utf-8'), columns=["details"])
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete_payment_items(self, rowkey) -> bool:
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                tbl.delete(rowkey.encode('utf-8'), columns=["items"])
            return True
        except Exception as e:
            print(e)
        return False
           
    def select_record_cols_id(self, rowkey, cols:List[str]):
        try:
            with self.pool.connection() as conn:
               tbl:Table = conn.table("payments")
               cols = [c.encode('utf-8') for c in cols]
               row = tbl.row(rowkey.encode('utf-8'), cols)
            records = {key.encode('utf-8'):value.encode('utf-8') for key, value in row[1].items()}
            return records
        except Exception as e:
            print(e)
        return None
    
    def select_records_ids(self, rowkeys:List[str], cols:List[str] = None):
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                if cols == None or len(cols) == 0:
                    rowkeys = tbl.rows(rowkeys)
                    rows = [rec[1] for rec in rowkeys]
                else:
                    rowkeys = tbl.rows(rowkeys, cols)
                    rows = [rec[1] for rec in rowkeys]
            records = list()
            for r in rows:
                records.append({key.decode():value.decode() for key, value in r.items()})
            return records
        except Exception as e:
            print(e)
        return None
    
    def select_records_tutor(self, tutor_id):
        records = []
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                datalist = tbl.scan(columns=["details", "items"], filter="SingleColumnValueFilter('details', 'tutor_id', =,'binary:{}')".format(tutor_id))
                for key, data in datalist:
                    data_str = {k.decode(): v.decode() for k, v in data.items()}
                    records.append(data_str)
            return records
        except Exception as e:
            print(e)
        return records
    
    def select_all_records(self):
        records = []
        try:
            with self.pool.connection() as conn:
                tbl:Table = conn.table("payments")
                datalist = tbl.scan(columns=['details', 'items'])
                for key, data in datalist:
                    data_str = {k.decode(): v.decode() for k, v in data.items()}
                    records.append(data_str)
                return records
        except Exception as e:
            print(e)
        return records