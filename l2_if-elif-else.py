# Requesting user's work experience
work_experience = int(input("Enter your full work experience in years: "))

# Determine the developer's skill level
if work_experience < 2:
    developer_type = "Junior"
elif 1 <= work_experience <= 5:
    developer_type = "Middle"
else:
    developer_type = "Senior"

# Output
print("Developer level:", developer_type)