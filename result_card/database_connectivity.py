import mysql.connector
def database():
    conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
    cur_obj = conn.cursor()
    try:
        cur_obj.execute('create database result')
        cur_obj.execute('use result')
        return cur_obj
    except:
        cur_obj.execute('use result')
        return cur_obj