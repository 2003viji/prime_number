# prime number-   It's devisible by one and itself

num=int(input("Enter your value :"))
for i in range(num+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
