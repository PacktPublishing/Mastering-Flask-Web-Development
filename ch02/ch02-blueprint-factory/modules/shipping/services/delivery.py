from modules.shipping.repository.delivery_officer import DeliveryOfficerRepository

def get_all_did(db):
    repo = DeliveryOfficerRepository(db)
    recs = repo.select_all()
    ids = [(rec.id, f'{rec.lastname}, {rec.firstname} {rec.middlename}') for rec in recs]
    return ids