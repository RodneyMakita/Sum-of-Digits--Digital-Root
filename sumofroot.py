def digital_root(n):
    while n>=10:
        n=sum(int(digit)for digit in str(n))
    return n

number=int(input('Input Your Number My Dear LEGEND: '))
result=digital_root(number)
print("Your Input is: ",number,"\nYour Output Is: ",result)
