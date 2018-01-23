num=int(input("no: "))
a=0
for i in range(1,num):
    if num%i==0:
        a=a+i
print("sum is {}".format(a))
if a==num:
    print("perfect number")
else :
    print("not a perfect number")
