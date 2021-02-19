'''<yasir_ahmad>
WAP to create a file named as 'student.txt' which will contain names of 'n' number of students.Then create another file 'copy.py' in which copy
only those names from 'student.txt' that starts with letter 'A'.
'''
f=open('student.txt','w+')
for i in range(int(input('Enter number of students: '))):
    f.write(input('Enter name: ')+str('\n'))
f.seek(0,0)

c=open('copy.txt','w')
for i in f.readlines():
    if i[0]=='A':
        c.write(i)

c.close()
f.close()