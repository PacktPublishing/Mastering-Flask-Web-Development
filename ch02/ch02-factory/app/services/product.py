from app.repository.product import ProductRepository


def get_all_pid(db):
    repo = ProductRepository(db)
    recs = repo.select_all()
    ids = [(p.id, p.name) for p in recs]
    return ids

