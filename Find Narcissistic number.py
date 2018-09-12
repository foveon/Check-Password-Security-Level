# find all the narcissistic number between 100 and 1k
for i in range(100,1000):
    if i==((i//100)**3)+((i//10)%10)**3+((i%10)%10)**3:
        print(i)
    else:
        i=i+1
        
    
