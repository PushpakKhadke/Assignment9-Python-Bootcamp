# 5. Write a python script to print first N odd natural numbers in reverse order.

Number=int(input("Enter the Number: "))
i=1
while i<=Number:
    print(Number*2-1,end=" ")
    Number-=1
print()
