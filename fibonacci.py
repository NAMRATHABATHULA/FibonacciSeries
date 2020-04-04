nterms=int(input("Number of terms to be displayed from the serirs? "))
a=0
b=1
count=0
while count<nterms:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
