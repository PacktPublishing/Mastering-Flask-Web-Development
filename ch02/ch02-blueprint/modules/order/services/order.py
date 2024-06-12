from modules.order.repository.order import OrderRepository

def get_all_order_no(db):
    repo = OrderRepository(db)
    recs = repo.select_all()
    orders = [o.order_no for o in recs]
    return orders