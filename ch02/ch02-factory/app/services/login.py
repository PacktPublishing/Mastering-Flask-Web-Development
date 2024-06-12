from app.repository.login import LoginRepository


def get_login_id(utype:int, db):
    repo = LoginRepository(db)
    records = repo.select_login_id_name(utype)
    return records