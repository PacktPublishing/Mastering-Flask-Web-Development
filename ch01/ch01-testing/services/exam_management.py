from repository.question_pool import insert_question_pool, get_current_id
from repository.question_choices import insert_question_choice
from repository.question_subjective import insert_question_subjective
from repository.question_details import select_all_question_details
from typing import Dict, Any, List

def add_exam_items(qid:int, qtype:int, question:str, params:Dict[str, Any]=None, ans_essay:str=None,answers: List[str]=None) -> bool:
    try:
        insert_question_pool(question=question, type=qtype, qid=qid) 
        curr_id = get_current_id()
        if qtype == 1:
            correct_answer = False
            for key, val in params.items():
                if key in answers:
                    correct_answer = True
                insert_question_choice(qid=qid, item_id=curr_id[0], choice=key, choice_text=val, correct_choice=correct_answer)
                correct_answer = False
        elif qtype == 2:
            insert_question_subjective(qid=qid, item_id=curr_id[0], correct_answer=ans_essay)
        return True
    except Exception as e:
        print(e)
    return False


def list_exam_details():
    exams = select_all_question_details()
    return exams
   