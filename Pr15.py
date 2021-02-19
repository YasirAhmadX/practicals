'''<yasir_ahmad>
WAP to enter the details of 'n' number of students having their roll,age,name in the form of a nested list, dump the entire dataset
in a file 'students.txt',then display back only those records from that file whose age is more than 16 years.
'''
from pickle import dump,load
f=open('students.txt','w+b')
for i in range(int(input('Number of students: '))):
    l=[int(input('Enter roll: '))]
    l.append(int(input('Enter age of roll '+str(l[0])+':')))
    l.append(input('Enter name of roll '+str(l[0])+':'))
    dump(l,f)
    
f.seek(0,0)
data=load(f)
try:
    while data:
        if data[1]>16:
            print(data)
        data=load(f)
except:
    pass
finally:
    f.close() 