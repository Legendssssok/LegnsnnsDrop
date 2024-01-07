from drop.database.all_db import legend_db


def get_time():
    return legend_db.get_key("TIME") or {}

def clean_time():
    tusers = {}
    return legend_db.set_key("TIME", tusers)
    
def add_time(id, time):
    tusers = get_time()
    tusers[id] = time
    return legend_db.set_key("TIME", tusers)
