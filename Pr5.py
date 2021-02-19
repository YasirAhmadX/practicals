'''<yasir_ahmad>
Write a program to input n numbers of integer in  a list and print the maximum even numberr present in it , if no even number is present, then
print('No even numbers is present !')
'''
l=[]
for i in range(int(input('Enter no. of entries: '))):
    l.append(int(input()))

evn_number=-1 #-1 is default value, will channge once an even number is found.
for i in l:
    if i%2==0 and i>evn_number:
        evn_number=i

print('No even number is present.' if evn_number==-1 else evn_number)
