'''<yasir_ahmad>
WAP to input a list having 'n' number of elements and print the sum of all prime numbers and all odd numbers.
'''
l=[]
for i in range(int(input('Enter no. of elements in the list: '))):
    l.append(int(input('Enter element: ')))
sum_odd=sum_prime=0
for i in l:
    j=0
    prime=True
    
    for d in range(2,i//2 +1):
        if i%d==0 or i==1:
            prime=False
    if prime:
        sum_prime+=i

    if i%2!=0:
        sum_odd+=i
    
print('sum of odd no. is: ',sum_odd)
print('sum of prime no. is: ',sum_prime)