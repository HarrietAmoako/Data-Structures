import numpy as np
L=12#length of beam in meters
W=10#intensity of load in KN/M
#Question a
#Bending moment(m) and shear force(v) at the first end,x=0
X=0
M=(W*(-6*X**2+6*L*X-L**2))/12
V=W*(L/2-X)
I='The bending moment at x=0 is'
J='the shear force at x=0 is'
print()
print('(a.1)'+I+str(M)+'and',J+str(V))
#Bending moment(M) and shear force(V) at the first end,X=L=10
X=L
M=(W*(-6*X**2+6*L*X-L**2))/12
V=W*(L/2-X)
a='The bending moment at X=L is'
b='the shear force at X=L is'
print()
print('(a.2)'+I+str(M)+'and',J+str(V))
#Question b
"""
When the bending moment is zero,we get an expression X**2-LX+L**2/6=0
"""
#from the expression
a=1
b=-L
c=L**2/6
#Using the almighty formula,the two roots are;
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print()
print('(b) The points of contra-flexure are {0} and {1}'.format(root_1b,root_2b))
#Question c
"""
When the shear force is zero,X=L/2
"""
X=L/2
print()
print('(c) The point at which V=0 is {}'.format(X))
#Question d
p=0
s=0.01
q=L+s
X=np.arange(p,q,s)
M=(W*(-6*X**2+6*L*X-L**2))/12
print()
print('(d) Using the initialized variable,the bending at each step in the array is{0}'.format(V))
#Question e
V=W*(L/2-X)
print()
print('(e) The shear force for each step along the span is {}'.format(V))
#Question f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be I_AM
"""
AM=abs(M)
I_AM=min(AM)
"""
When the bending moment is I_AM,we get an expression X**2-LX+(L**2/6)+(2*I_AM)/W=0
"""
#from the above expression
a=1
b=-L
c=(L**2/6)+(2*I_AM)/W
#Using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1f=(-b+np.sqrt(discriminant))/2*a
root_2f=(-b-np.sqrt(discriminant))/2*a
print()
print('(f) The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))
#Question g
"""
Let the relative errors be r_e
"""
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2f-root_2b)/root_2f*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_e1,r_e2))
#Question h
"""
Let the maximum bending moment be max_M and the minimum bending moment be min_M
"""
#for the maximum
max_M=max(M)
"""
When the bending moment is max_M,we get an expression X**2-LX+(L**2/6)+(2*max_M)/W=0
"""
a=1
b=-L
c=(L**2/6)+(2*max_M)/W
#Using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print()
print('(h.1) The points at which the maximum bending moment occur are {0} and {1}'.format(root_1,root_2))
#for the minimum
print()
print('(h.2) The points at which the minimum bending moment occur are{0}and {1}'.format(root_1,root_2))
min_M=min(M)
"""
When the bending moment is min_M,we get an expression X**2-LX+(L**2//6)+(2*min_M)/W=0
"""
a=1
b=-L
c=(L**2//6)+(2*min_M)/W
#Using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b-np.sqrt(discriminant))/2*a
root_2=(-b+np.sqrt(discriminant))/2*a
print()
print('(h.2) The points at which the bending moment occur are {0} and {1}'.format(root_1,root_2))
#Link to github account
#https://github.com/HarrietAmoako




