#input
name = input("What is your name? ")
age = input("What is your age? ")
  

with open("user_info.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
