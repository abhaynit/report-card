import json
book = {}
book['cse'] = {
                #'sem1':[['SH101','English - I',3,0,0,3],['MA101','Engineering Mathematics - I',3,1,0,4]],
                'sem1':[['SH101','English - I',3,0,0,3],['MA101','Engineering Mathematics - I',3,1,0,4],['PH101','Engineering Physics - I',3,0,0,3],['CY101','Engineering Chemistry',3,0,0,3],['GE101','Engineering Graphics',3,1,0,4],['GE102','Introduction to Computing',3,0,0,3],['PH102','Physics Laboratory - I ',0,0,2,1],['CY102','Chemistry Laboratory',0,0,2,1],['GE103','Computer Programming Laboratory',0,0,3,2]],
                'sem2':[['SH151','English - II', 3, 0, 0, 3],['MA151', 'Engineering Mathematics - II',3,1,0,4],['PH151','Engineering Physics - II',3,0,0,3],['GE151','Environmental Science and Engineering',3,0,0,3],['GE152','Engineering Mechanics',3,1,0,4],['CS151','Digital System Fundamentals',3,0,0,3],['PH152','Physics Laboratory - II',0,0,2,1],['GE153','Workshop',0,0,2,1],['CS152','Digital System Laboratory',0,0,3,2]],
                'sem3':[['MA202','Discrete Mathematics',3,1,0,4],['CS201','Data Structure',3,0,0,3],['CS202','Computer Architecture',3,0,0,3],['CS203','Database Management System',3,0,0,3],['EE208','Electrical Science',3,0,2,4],['CS204','Programming Paradigms',3,0,0,3],['CS205','Data Structure Laboratory',0,0,3,2],['CS206','Advanced Programming Laboratory',0,0,3,2],['CS207','Database Management System Laboratory',0,0,3,2]],
                'sem4':[['MA251','Numerical Methods',3,1,0,4],['CS255','Algorithmics Laboratory',0,0,3,2],['CS251','Algorithmics',3,0,0,3],['CS256','Microprocessors and Microcontrollers Laboratory',0,0,3,2],['CS252','Microprocessor and Microcontroller',3,0,0,3],['CS257','Operating System Laboratory',0,0,3,2],['CS253','Web Technology',2,0,2,3],['CS254','Operating System',3,0,0,3],['SH251','Engineering Economics',3,0,0,3] ],
                'sem5':[['CS301','Computer Graphics',3,0,0,3],['CS302','Digital System Fundamentals',3,0,0,3],['CS303','Formal Language And Automata Theory',3,0,0,3],['CS304','Computer Networks',3,0,0,3],['CS969','Python Programming',3,0,0,3],['CS903','Data Mining and Data Warehousing',3,0,0,3],['CS305','Computer Grphics Laboratory',0,0,3,2],['CS306','Digital Signal Processing Laboratory',0,0,3,2],['CS307','Computer Network Laboratory',0,0,3,2]]
                }
s = json.dumps(book)
with open ("abc.txt",'w') as f:
    f.write(s)