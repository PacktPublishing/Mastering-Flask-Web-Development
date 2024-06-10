from repository.counselor import select_all_counselor
from repository.patient import select_all_patient
from repository.question_details import select_all_question_details
from repository.user import select_all_user


def list_cid():
    print(select_all_counselor())
    cids = [id[1] for id in select_all_counselor()] 
    return cids

def list_pid():
    pids = [id[0] for id in select_all_patient()]
    return pids


def list_qid():
    qids = [id[0] for id in select_all_question_details()]
    return qids

def list_usernames():
    usernames = [id[1] for id in select_all_user()]
    return usernames
