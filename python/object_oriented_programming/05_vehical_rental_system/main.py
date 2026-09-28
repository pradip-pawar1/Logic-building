
# ----------------||------------------
# check password to verify admin
def check_pass(passward:str) -> bool:
    if passward == "admin01":
        return True
    return False