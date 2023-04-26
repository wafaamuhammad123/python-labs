# 1-

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# print(last_name + " " + first_name)


# 2-

# n = int(input("Enter an integer: "))

# nn = n * 11
# nnn = n * 111
# result = n + nn + nnn

# print("The value of n+nn+nnn for n =", n, "is", result)

# 3-

# print("""a string that you "don't" have to escape
# This is a ....... multi-line
# heredoc string --------> example""")


# 4-

# import math
# radius = 6
# volume = (4/3) * math.pi * (radius ** 3)
# print("The volume of the sphere with radius", radius, "is", volume)


# 5-

# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area = 0.5 * base * height
# print("The area of the triangle with base", base, "and height", height, "is", area)


# 6-

# num_rows = 5
# for i in range(num_rows):
#     for j in range(i):
#         print("*", end="")
#     print("")

# for i in range(num_rows, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print("")



# 7-

# word = input("Enter a word: ")
# reversed_word = word[::-1]

# print("The reversed word is:", reversed_word)



# 8-

# for num in range(7):
#     if num == 3 or num == 6:
#         continue
#     print(num)


#  9-   


# a, b = 0, 1
# while a <= 50:
#     print(a, end=" ")
#     a, b = b, a + b


# 10-


string = input("Enter a string: ")

num_digits = 0
num_letters = 0

for char in string:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print("Number of digits:", num_digits)
print("Number of letters:", num_letters)