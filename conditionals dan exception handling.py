# Using If-Else
try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 3.80 <= your_GPA <= 4.0:
            print(f"Damn you've got a magna cumlaude with your {your_GPA} GPA")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
        elif 3.00 <= your_GPA < 3.50:
            print("You've got a stable GPA tho")
        else:  # berarti < 3.0
            print("You need a stable GPA")
    else:
        print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
    print("Please enter a valid GPA")


# Using match case
try:
    status_code = int(input("Enter your status code: "))
    print("Your code means:")

    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown Status Code")
except:
    print("Please enter a valid status code")

    #Ternary
a = 3
b = "Even Numbers" if a % 2 == 0 else "Odd Numbers"
print(b)

# Using Loops
for i in range(5):
    print(i)

# For loop with range
for i in range(5):
    print("Data science is easy!")

print("=" * 50)

for i in range(1, 5, 2):
    print("Data science is easy!")

# word
word = "I want to master data science"
for letter in word:
  print(letter)

# You can use it with enumerate function
for m, n in enumerate(word):
 print(f"Index {m}. {n}")

 # It can go backwards
for i in range(5,1,-1):
 print("I want big data's")


# Keyword control
for i in range(5):
    if i == 2:
        continue  # skip this loop when i is equal to 2
    if i == 4:
        break     # stops the loop when i is equal to 4
    print(i)

    #Using while loop
count = 0
while count < 4:
 print("Keep the spirits up interns!")
count += 1
