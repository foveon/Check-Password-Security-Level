# A trimorphic number is a number whose cube ends in the number itself
# the program list all the trimorphic numbers in a give range(10000).
for a in range(10000):
    b=int(len(str(a)))
    if (a**3)%(10**b) == a:
        print(a)
    else:
        a=a+1


    

