a=[1,2,3,4,5,6,7,9]

def get_missing_number(a):
    n= a[-1] #assigning the last number so that it can do sum of nth natural number
    sum1=0
    sum2 = n*(n+1)/2
    for i in a:
        sum1 = sum1 + i
    missing_number = sum2 - sum1
    print("The missing number is",missing_number)

get_missing_number(a)


        
    
