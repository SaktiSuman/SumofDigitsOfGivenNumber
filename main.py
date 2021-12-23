n = int(input("Enter a number: "))
sum = 0;
while(n):
    r = n % 10
    sum = sum + r
    n = n // 10
print(sum)