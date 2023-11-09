from drop.database.all_db import legend_db


def get_store():
    return legend_db.get_key("STORE") or []


def is_store(file):
    return file in get_store()


def add_store(file):
    tusers = get_store()
    if not file in tusers:
        tusers.append(file)
        return legend_db.set_key("STORE", tusers)
    return False


def del_store(file):
    if is_store(file):
        tusers = get_store()
        tusers.remove(file)
        return legend_db.set_key("STORE", tusers)
    return False

def clean_store():
    tusers = []
    return legend_db.set_key("STORE", tusers)
