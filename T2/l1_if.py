is_next = None

# Input validation
while True:
    user_input = input("Enter number points: ")
    if user_input.isdigit():
        num = int(user_input)
        break
    else:
        print("Error! use integers only")

# Verification logic
if num >= 83:
    is_next = True
else:
    is_next = False
    
# output of the result
if is_next:
    print(is_next, " Проходить до наступного туру")
else:
    print(is_next, " Не проходить до наступного туру")
    
    