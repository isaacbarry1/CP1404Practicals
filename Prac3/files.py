# Question 1
name = input("Please enter your name: ")
output_file = open('name.txt', 'w')
print(name, file=output_file)
output_file.close()

# Question 2
namefile = open("name.txt", 'r')
name = namefile.read().strip()
print(f"Your name is {name}")
namefile.close()

# Question 3
in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

# Question 4
in_file = open('numbers.txt', 'r')
# Creating variables
i = 0
total = 0
# This function goes through the file and makes 1 equal every line and adds it to the previous total
for i in in_file:
    number = int(i)
    total += number
print(total)
in_file.close()
