from drop.database.all_db import legend_db


def get_users():
    return legend_db.get_key("USERS") or []


def is_users(id):
    return id in get_users()


def add_users(id):
    tusers = get_users()
    if not id in tusers:
        tusers.append(id)
        return legend_db.set_key("USERS", tusers)
    return False


def del_users(id):
    if is_users(id):
        tusers = get_users()
        tusers.remove(id)
        return legend_db.set_key("USERS", tusers)
    return False
