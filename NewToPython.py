print("Hello World")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "Tom"
character_age = "50"
is_male = False
phrase = "this is the best"
print("There was a man named " + character_name + ", ")
print("He was " + character_age + " years old.")
print("He really\"liked the name " + character_name + ", ")
print("but didn't\nlike being " + character_age + ".")
print(phrase + " and cool")
print(phrase.islower())
print(phrase.upper())
# makes phrase upper case then checks if all chars are upper case
print(phrase.upper().isupper())
print(len(phrase)) # returns string length
print(phrase[0]) # return character in the string at position 0
print(phrase.index("b")) # oposite of above
print(phrase.index("best")) # oposite of above
print(phrase.replace("best", "cool"))
# numbers
print(13 % 4)
my_num = 5
print(my_num)
print("Number is " + str(my_num))
print(abs(-9))
print(pow(3, 2.4))
print(max(4, 6))
print(min(4, 6))
print(round(3.7))
from math import *
print(floor(3.7))
#name = input("Enter your name: ")
#print("Hello " + name + "!")
#age = input("Enter your age: ")
#print("Hello " + name + "! You are " + age)
#num1 = input("Enter the first number: ")
#num2 = input("Enter the second number: ")
#sums = float(num1) + float(num2)
#print(sums)
friends = ["kevin", "Ray", "Tom"]  # Lists
print(friends[1:])
friends.append("John")
lucky_numbers = [4, 8, 15, 16, 16, 3, 12]
friends.extend(lucky_numbers)
print(friends)

friends.insert(1, "Kelly")
friends.remove("Ray")
print(friends)

print(friends.pop())
print(friends)
print(friends.index("Tom"))
print(friends.count(16))
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
friends.clear()

coordinates = [(4, 5), (6, 7)]  # Tuple (constant list)


def say_hi(name):
    print("\nHello " + name)


say_hi("Mike")
say_hi("Steve")


def cube(num):
    return num * num * num


print(cube(3))
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a not a male but are tall")
else:
    print("You are not male and not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 40, 5))

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

# Dictionary
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversion["Feb"])
print(monthConversion.get("Feb", "Not a valid month"))
print(monthConversion.get("Aug", "Not a valid month"))

i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

secret_word = "l"  # leopard
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You LOSE! ")
else:
    print("You WIN!")

friends = ["Jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

len(friends) # length of array
for index in range(len(friends)):
    print(friends[index])

print(2.23**12.71)  # power


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 5))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

# Exceptions
try:

    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

# reading and writing, r = just reading
employee_file = open("employees.txt", "r+")

# Whether or not the file is readable -> Boolean
print(employee_file.readable())

print(employee_file.readline())  # read the first line
print(employee_file.readline())  # read the second line
# put all lines in an array an access words as array elements
print(employee_file.readlines())

# printing out each line in the file
for employee in employee_file.readlines():
    print(employee)
#  append
employee_file = open("employees.txt", "a")
employee_file.write("\nJohn - HR")

#  create new file
employee_file = open("employees1.txt", "w")

#  write html code inside python
employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")

employee_file.close()

import Module1
print(Module1.roll_dice(10))

import docx
docx.Document()

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.8, True)

print(student1)
print(student1.name)
print(student1.gpa)

question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

from Question import Question

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)

print(student1.on_honor_roll())
print(student2.on_honor_roll())

#  Inheritance

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()

myChineseChef.make_special_dish()


