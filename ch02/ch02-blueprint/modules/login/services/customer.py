from modules.login.repository.customer import CustomerRepository

def get_all_cid(db):
    repo = CustomerRepository(db)
    recs = repo.select_all()
    ids = [(rec.id, f'{rec.lastname}, {rec.firstname} {rec.middlename}') for rec in recs]
    return ids