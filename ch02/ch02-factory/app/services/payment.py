from app.repository.payment import PaymentRepository


def get_all_payid(db):
    repo = PaymentRepository(db)
    recs = repo.select_all()
    ids = [(rec.id, rec.ref_no ) for rec in recs]
    return ids
    