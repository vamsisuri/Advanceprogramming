l1=[" ","one","Two","Three","Fou","Five","Six","Seven","Eight","Nine"]
l2=[" ","Ten","Twenty","Thirty","Fourty","fifty","Sixty","seventy","Eighty","Ninty"]
l3=[" ","Eleven","Tweleve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n=int(input("Enter the number:"))
l=[]
if n>=100:
    r1=n//100
    l.append(l1[r1])
    p = n%100
    p1=p//100
    l.append(l2[p1])
if n<20:
    r2=n//10
    l.append(l3[r2])
    p = n%20
    p3 = p//20
    l.append(l2[p3])
elif p >=20:
    p1 = p//10
    l.append(l2[p1])
    print(l)
else:
    print(None)




# else:
#     print(None)


