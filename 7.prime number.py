s=int(input("Enter the starting number:"))
e=int(input("Enter the ending number:"))
for i in range(s,e+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
