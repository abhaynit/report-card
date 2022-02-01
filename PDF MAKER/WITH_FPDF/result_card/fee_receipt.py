from datetime import date
from fpdf import FPDF
from database_connectivity import database

def print_result(registration_no,sem,branch):
    #initializing the variable
    registration_no = int(registration_no)
    sem = int(sem) 
    branch = str(branch)

    #adding page to pdf documents
    pdf = FPDF()
    pdf.add_page()

    #max size is 190
    #upper name and logo
    pdf.image('E:/old/old e drive/ABHAY/PDF MAKER/WITH_FPDF/result_card/logo.png', x=10, y=5, w=30)
    pdf.image('E:/old/old e drive/ABHAY/PDF MAKER/WITH_FPDF/result_card/nitnaga.png', x=80, y=7, w=80)
    pdf.set_font('Arial','B',16)
    pdf.text(50,20,'NATIONAL INSTITUTE OF TECHNOLOGY NAGALAND')
    pdf.set_font('Arial','B',13)
    pdf.text(80,25,'Chumukedima, Dimapur - 797103')
    pdf.text(100,30,'Nagaland')

    #background image
    #pdf.image('lightlogo.png', x=38, y=70, w=150)
    #pdf.image('C:/Users/abhay/datascience/flower_image_altered.png',x=38,y=70,w=150)

    #line draw
    pdf.line(10,85,10,184.5)
    pdf.line(27,85,27,184.5)
    pdf.line(44,85,44,184.5)
    pdf.line(130,85,130,184.5)
    pdf.line(153,85,153,184.5)
    pdf.line(176,85,176,184.5)
    pdf.line(200,85,200,184.5)

    epw = pdf.w - 2*pdf.l_margin
    
    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw,60, 'PROVISIONAL RESULT', align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(40)

    #database connectivity
    
    import mysql.connector
    conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
    cur_obj = conn.cursor()
    cur_obj.execute('use result')
    
    #query for getting the student data
    query1 = 'select * from student_detail where reg_no = %s'
    cur_obj.execute(query1,(registration_no,))
    for i in cur_obj:
        # Text height is the same as current font size
        th = pdf.font_size*2.5
        pdf.set_font('Times','B',8.0)
        pdf.cell(34,th,'NAME OF CANDIDATE',1,0,'C')
        pdf.cell(86,th,str(i[1]).upper(),1,0,'C')
        pdf.cell(40,th,'REGISTRATION NO ',1,0,'C')
        pdf.cell(30,th,str(i[0]),1,0,'C')
        pdf.ln(th)

        #SECOND ROW
        import datetime
        pdf.cell(34,th,'DATE OF BIRTH',1,0,'C')
        date_values = str(i[3]).split('-')
        if date_values[1][0]!='0':
            mon = date_values[1]
        else:
            mon = date_values[1][1]

        if date_values[2][0]!='0':
            da = date_values[2]
        else:
            da = date_values[2][1]
        x = datetime.date(int(date_values[0]),int(mon) , int(da))

        pdf.cell(26,th,str(x.strftime("%d %b %Y")),1,0,'C')
        pdf.cell(30,th,'GENDER',1,0,'C')
        pdf.cell(30,th,str(i[2]),1,0,'C')
        query1 = 'select * from marks where reg_no = %s and semester = %s'
        cur_obj.execute(query1,(registration_no,sem))
        month_year_of_exam = ''
        for value in cur_obj:
            month_year_of_exam =   value[2]
        pdf.cell(40,th,'MONTH & YEAR OF EXAM ',1,0,'C')
        pdf.cell(30,th,str(month_year_of_exam),1,0,'C')
        pdf.ln(th)

        #third row
        pdf.cell(34,th,'BRANCH',1,0,'C')
        pdf.set_font('Times','B',10.0)
        pdf.cell(86,th,str(i[4]),1,0,'C')
        pdf.set_font('Times','B',8.0)
        pdf.cell(40,th,'DATE OF PUBLICATION ',1,0,'C')
        q = datetime.date.today()
        pdf.cell(30,th,str(q.strftime("%d %b %Y")),1,0,'C')

    pdf.ln(th)

    #fourth row 
    pdf.set_font('Times','B',6.0) 
    pdf.cell(17,th,'SEMESTER NO',1,0,'C')
    pdf.cell(17,th,'COURSE CODE',1,0,'C')
    pdf.cell(86,th,'COURSE TITLE ',1,0,'C')
    pdf.cell(23,th,'CREDIT',1,0,'C')
    pdf.cell(23,th,'LETTER GRADE',1,0,'C')
    pdf.cell(24,th,'POINT',1,0,'C')
    pdf.ln(th)

    pdf.set_font('Times','B',8.0) 
    count =0

    import json
    f = open('abc.txt','r')
    s = f.read()
    book = json.loads(s)
    final_value = book[branch]['sem'+str(sem)]

    point = {'s':10,'a':9,'b':8,'c':7,'d':6,'e':5,'f':'','u':'','ab':'','':''}

    query1 = 'select * from marks where reg_no = %s and semester = %s'
    cur_obj.execute(query1,(registration_no,sem))
    for value in cur_obj:
        for i in range (len(final_value)):
            pdf.set_font('Times','B',10.0)
            pdf.cell(17,th,str(value[1]),0,0,'C')
            pdf.cell(17,th,str(final_value[i][0]),0,0,'C')
            pdf.cell(86,th,str(final_value[i][1]),0,0,'C')
            pdf.cell(23,th,str(final_value[i][5]),0,0,'C') 
            pdf.cell(23,th,str(value[3+i]).upper(),0,0,'C')
            pdf.cell(24,th,str(point[str(value[3+i]).lower()]),0,0,'C')
            pdf.set_font('Times','B',8.0) 
            pdf.ln(th)
            count+=1

    if count!=9:
        for i in range(9-count):
            pdf.ln(th)

    
    pdf.ln(20)
    pdf.set_font('Times','B',7.0)
    #first row
    pdf.cell(34,th,'SEMESTER',1,0,'C')
    pdf.cell(19.5,th,'|',1,0,'C')
    pdf.cell(19.5,th,'||',1,0,'C')
    pdf.cell(19.5,th,'|||',1,0,'C')
    pdf.cell(19.5,th,'|V',1,0,'C')
    pdf.cell(19.5,th,'V',1,0,'C')
    pdf.cell(19.5,th,'V|',1,0,'C')
    pdf.cell(19.5,th,'V||',1,0,'C')
    pdf.cell(19.5,th,'V||',1,0,'C')
    pdf.ln(th)
    
    #second row
    pdf.cell(34,th,'CREDIT REGISTERED',1,0,'C')
    credit_registered = []
    credit_gain = []
    for i in range(int(sem)):
        qwe = []
        f = open('abc.txt','r')
        s = f.read()
        book = json.loads(s)
        final_value = book[branch]['sem'+str(i+1)]
        calcu = 0
        for j in final_value:
            calcu+=j[5]
            qwe.append(int(j[5]))
        credit_registered.append(str(calcu))
        credit_gain.append(qwe)
    if len(credit_registered)<8:
        for i in range(8-len(credit_registered)):
            credit_registered.append('-')
    print(credit_registered)
    print(credit_gain)

    pdf.cell(19.5,th,credit_registered[0],1,0,'C')
    pdf.cell(19.5,th,credit_registered[1],1,0,'C')
    pdf.cell(19.5,th,credit_registered[2],1,0,'C')
    pdf.cell(19.5,th,credit_registered[3],1,0,'C')
    pdf.cell(19.5,th,credit_registered[4],1,0,'C')
    pdf.cell(19.5,th,credit_registered[5],1,0,'C')
    pdf.cell(19.5,th,credit_registered[6],1,0,'C')
    pdf.cell(19.5,th,credit_registered[7],1,0,'C')
    pdf.ln(th)
    
    #THIRD ROW
    pdf.cell(34,th,'CREDIT EARNED',1,0,'C')
    pdf.cell(19.5,th,credit_registered[0],1,0,'C')
    pdf.cell(19.5,th,credit_registered[1],1,0,'C')
    pdf.cell(19.5,th,credit_registered[2],1,0,'C')
    pdf.cell(19.5,th,credit_registered[3],1,0,'C')
    pdf.cell(19.5,th,credit_registered[4],1,0,'C')
    pdf.cell(19.5,th,credit_registered[5],1,0,'C')
    pdf.cell(19.5,th,credit_registered[6],1,0,'C')
    pdf.cell(19.5,th,credit_registered[7],1,0,'C')
    pdf.ln(th)
    
    #FOURTH ROW
    grade_point_average = []
    """
    import mysql.connector
    conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
    cur_obj = conn.cursor()
    cur_obj.execute('use result')
    """
    point1 = {'s':10,'a':9,'b':8,'c':7,'d':6,'e':5,'f':0,'u':0,'ab':0,'':0}
    query1 = 'select sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9 from marks where reg_no = %s and semester = %s'
    for i in range(int(sem)):
        cur_obj.execute(query1,(int(registration_no),int(i+1)))
        calc = 0
        for k in cur_obj:
            print(k)
            for j in range(len(k)):
                try:
                    calc+=point1[str(k[j]).lower()]*int(credit_gain[i][j])
                except:
                    pass
            grade_point_average.append(str(round(calc/int(credit_registered[i]),2)))
        
    if len(grade_point_average)!=8:
        for i in range(8-len(grade_point_average)):
            grade_point_average.append("##")

    pdf.cell(34,th,'GRADE POING AVERAGE',1,0,'C')
    pdf.cell(19.5,th,grade_point_average[0],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[1],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[2],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[3],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[4],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[5],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[6],1,0,'C')
    pdf.cell(19.5,th,grade_point_average[7],1,0,'C')
    pdf.ln(th)

    #FIFTH ROW
    pdf.cell(34,th,'TOTAL CREDIT EARNED',1,0,'C')
    pdf.cell(19.5,th,'',1,0,'C')
    pdf.cell(136.5,th,'CUMULATIVE GRADE POING AVERAGE (CGPA)',1,0,'L')
    
    pdf.output("result.pdf")
#print_result(2019105194,3,'cse')