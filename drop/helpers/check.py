def check_sudo(user_id):
    if user_id in SUDO_USERS:
        return True
    return False
