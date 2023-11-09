from drop.database.all_db import legend_db


def get_time():
    return legend_db.get_key("TIME") or {}


def add_store(id, time):
    tusers = get_time()
    tusers[id] = time
    return legend_db.set_key("TINE", tusers)
