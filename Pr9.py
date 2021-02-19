'''<yasir_ahmad>
WAP to create a function which takes 3 arguments (say a,b,ch) where a is length ;b is breadth and ch  is choice whether to compute area or perimeter.
Note:- Use keyword arguments:
    ch==1 for area
    ch==2 for perimeter
'''
def Area_Perimeter(a,b,ch):
    """
        a(int): Length of the rectangle
        b(int): Breadth of the rectangle
        ch(int): choice
                ch==1>>Area
                ch==2>>Perimeter
        Returns area or perimeter of the rectangle.
    """
    if ch==1:
        return 'Area is '+str(a*b)
    elif ch==2:
        return 'Perimeter is '+str(2*(a+b))
    else:
        return 'Invalid choice.'
x,y,choice=int(input('a: ')),int(input('b: ')),int(input('choice: '))
print(Area_Perimeter(a=x,ch=choice,b=y))
#help(Area_Perimeter)