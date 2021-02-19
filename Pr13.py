'''<yasir_ahmad>
WAP to read a text file 'student.txt' and count:
i)how many words are there that start with a vowel
ii)how many line start with T
iii)how many digits are there
'''
f=open('student.txt','r')
c_vowel=c_Tline=c_digits=0

for line in f.readlines():
    if line[0]=='T':
        c_Tline+=1
    for word in line.split():
        if word[0].lower() in ['a','e','i','o','u']:
            c_vowel+=1
        elif word.isdigit():
            c_digits+=1
f.close()
print('Number of lines that start with "T":',c_Tline)
print('Number of words tha start with a vowel:',c_vowel)
print('Number digits:',c_digits)
