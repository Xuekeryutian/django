if __name__=='__main__':
    import pymysql
    db = pymysql.connect('127.0.0.1','test44','cai6205278','xueker')
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    db.close()