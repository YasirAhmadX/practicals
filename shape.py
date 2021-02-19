'''<Pr11.shape.py><Pr12.shape.py><yasir_ahmad>
Create a module named as 'shape.py' which consists of three functions named as arear(),areas() and areac() for finding area of rectangle,square and circles resectively.
Call all these function from another file named as 'check.py'<pr11:call using accession operator><pr12:call without using accession operator>
'''
def arear(length,breadth):
    '''
        Return area of a rectangle of given length and breadth
    '''
    return length*breadth

def areas(side):
    '''
        Return area of a square of given side
    '''
    return side**2

def areac(radius):
    '''
        Return area of a circle of given radius
    '''
    from math import pi
    return pi*radius**2
