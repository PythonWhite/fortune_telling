def query_to_dict(query):
    dictret = dict(query.__dict__)
    dictret.pop("_sa_instance_state", None)
    return dictret


def dict_querys(query):
    return [query_to_dict(q) for q in query]


def check_login():
    pass


def write_rsponse(data=None, code=0, msg="success"):
    pass
