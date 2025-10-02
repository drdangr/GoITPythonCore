# input validation    
while True:
    try:
        num = int(input("Enter the integer (0 to 100): "))
        if 0 <= num <= 100:
            break
        print("Error: enter an integer from 0 to 100.")
    except ValueError:
        print("Error: enter an integer.")

sum = 0

# work cycle
while num > 0:
    sum += num
    num -= 1

print(sum)