from repository.patient_score import insert_patient_score, select_all_patient_score
from typing import Dict, Any

def record_patient_exam(formdata:Dict[str, Any]) -> bool:
    try:
        pct = round((formdata['score'] / formdata['total']) * 100, 2)
        print(pct)
        status = None
        if (pct >= 70):
            status = 'passed'
        elif (pct < 70) and (pct >= 55):
            status = 'conditional'
        else:
            status = 'failed'
        insert_patient_score(pid=formdata['pid'], qid=formdata['qid'], score=formdata['score'], total=formdata['total'], status=status, percentage=pct )
        return True
    except Exception as e:
        print(e)
    return False

def list_passing_scores(rating:float):
    exams = [rec for rec in select_all_patient_score() if rec[6] >= rating]
    return exams