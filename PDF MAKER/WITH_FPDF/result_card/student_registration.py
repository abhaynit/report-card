import mysql.connector
def marks_addition(reg_no,sem,mye,sub1='',sub2='',sub3='',sub4='',sub5='',sub6='',sub7='',sub8='',sub9=''):
    try:
        conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
        cur_obj = conn.cursor()

        cur_obj.execute('use result')


        query1 = 'insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur_obj.execute(query1,(int(reg_no),int(sem),str(mye),str(sub1),str(sub2),str(sub3),str(sub4),str(sub5),str(sub6),str(sub7),str(sub8),str(sub9)))
        conn.commit()
        return 1 
    except:
        return 0

def registration(reg_no,name,gender,dob,branch):
    try:
        conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
        cur_obj = conn.cursor()

        cur_obj.execute('use result')


        query1 = 'insert into student_detail values(%s,%s,%s,%s,%s)'
        cur_obj.execute(query1,(int(reg_no),str(name),str(gender),str(dob),str(branch)))
        conn.commit()
        return 1
    except:
        return 0

def marks_updation(reg_no,sem,sub1='',sub2='',sub3='',sub4='',sub5='',sub6='',sub7='',sub8='',sub9=''):
    try:
        conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
        cur_obj = conn.cursor()

        cur_obj.execute('use result')


        query1 = 'update marks set sub1=%s,sub2=%s,sub3=%s,sub4=%s,sub5=%s,sub6=%s,sub7=%s,sub8=%s,sub9=%s where reg_no = %s and semester = %s'
        cur_obj.execute(query1,(str(sub1),str(sub2),str(sub3),str(sub4),str(sub5),str(sub6),str(sub7),str(sub8),str(sub9),int(reg_no),int(sem)))
        conn.commit()
        return 1 
    except:
        return 0
        
def delete_registration(reg_no):
    #try:
        conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
        cur_obj = conn.cursor()

        cur_obj.execute('use result')


        query1 = 'delete from student_detail where reg_no = %s'
        cur_obj.execute(query1,(int(reg_no),))
        conn.commit()
        return 1
    #except:
        return 0


#registration(2019105217,'sudhir kumar','M','1998-3-7','Computer Science and Engineering')
#marks_addition(2019105217,5,'DEC 2021','b','A','b','B','b','b','s','A','a')
#marks_updation(2019105217,5,'DEC 2021','s','s','s','B','b','b','s','A','s')
#print(delete_registration(2019105217))

