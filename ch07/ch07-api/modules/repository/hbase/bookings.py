from typing import Dict, List, Any

class BookingRepository:
    
    def __init__(self, pool):
        self.pool = pool
    
    def upsert_booking(self, rowkey, tutor_id, stud_id, date_booked) -> bool:
        record = {'details:id' : str(rowkey), 'details:tutor_id': tutor_id, 'details:stud_id': stud_id, 'details:date_booked': date_booked}
        try:
            with self.pool.connection() as conn:
                tbl = conn.table("bookings")
                tbl.put(row=str(rowkey).encode(), data=record)
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete_record(self, rowkey) -> bool:
        try:
            with self.pool.connection() as conn:
                tbl = conn.table("bookings")
                tbl.delete(rowkey.encode())
            return True
        except Exception as e:
            print(e)
        return False
    
    def select_tutor_bookings(self, tutor_id):
        records = []
        try:
            with self.pool.connection() as conn:
                tbl = conn.table("bookings")
                datalist = tbl.scan(columns=["details"], filter="(SingleColumnValueFilter('details', 'tutor_id', =,'binary:{}')".format(tutor_id))
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
                tbl = conn.table("bookings")
                datalist = tbl.scan(columns=['details'])
                for key, data in datalist:
                    data_str = {k.decode(): v.decode() for k, v in data.items()}
                    records.append(data_str)
                return records
        except Exception as e:
            print(e)
        return records