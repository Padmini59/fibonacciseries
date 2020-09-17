a=int(input("how many terms?"))
n1, n2=0, 1
count = 0
if a <= 0:
    print("please enter a positive integer")
elif a == 1:
    print("fibonacci swquence upto",a,":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count < a:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count +=1


