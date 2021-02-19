'''<yasir_ahmad>
WPA to enter n number of registered user details in the form of dictionary, where the dictionary contain the following details 'userid:password'.
Ask the user to search any userid, if it is not present in the dictionary then print 'userid not registered', other wise check the corresponding,
password after asking the same from the user and print 'logged successfully' if the user enters the correct password otherwise print 
'incorrect password'.
'''

d={}
for i in range(int(input('Enter number of entries: '))):
    key=input('Enter userid: ')
    d[key]=input('Enter password: ')

s_userid=input('Enter userid to search: ')
s_passwd=input('Enter password: ')
if s_userid in d:
    if s_passwd == d[s_userid]:
        print('logged successfully.')
    else:
        print('incorrect password.')
else:
    print('userid not registered')
