def giveIDNo():
    cursor.execute("select ifnull(max(user_id),0) from tbl_user")
    maxid = cursor.fetchone()  
    IDNo = maxid[0] + 1
    return IDNo

