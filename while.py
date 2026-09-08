'''
1) WAP TO DIAPLAY FACTORS OF A GIVEN NUMBER
num = int(input("Enter the number: "))
i = 1
out=[]
while i<=num:
    if num%i==0:
        out.append(i)
    i+=1
print(out)


2)WAP TO DISPLAY THE PERFECT NUMBER
num = int(input("Enter the number: "))
i = 1
out=0
while i<num:
    if num%i==0:
        out=out+i
    i+=1
if out==num:
    print('Entered number is perfect number')
else:
    print("not a perfect number")'''

#3) WAP TO DISPLAY FIBONACCI SERIES
'''
num = int(input("Enter the number: "))
a=0
b=1
i=0
while i<=num:
    print(a, end=' ')
    a,b=b,a+b
    i+=1
'''

#WAP TO CONSIDER A HOMOGGENEUS TUPLE OF INTEGERS AND DIVIDE 
#IT TO 2 OUTPUTS LIKE EVEN AND ODD

'''k=(1,2,3,4,5,6,7,6,8)
even=[]
odd=[]
i=0
while i<len(k):
    if k[i]%2==0:
        even.append(k[i])
    else:
        odd.append(k[i])
    i+=1
print(even)
print(odd)'''

#Fetch the string values in a list only if it consists of middle char in it

lst = ["apple","cat","Dog","juy"]
i=0
while i<len(lst):
    if len(lst[i])%2!=0:
        print(lst[i])
    i+=1