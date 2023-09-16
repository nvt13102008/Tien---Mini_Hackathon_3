## Bai1.1
# def is_even(num):
#   return num % 2 == 0

# num = int((input("Input a number: ")))
# even = is_even(num)
# if is_even(num):
#   print("This number is even")
# else:
#   print("This number is not even")

## Bai1.2
# def cal_area(r):
#   return r * r * 3.14

# r = int(input("Input radius"))
# area = cal_area(r)
# print("Circle area:", area)

##Bai1.3
# def reverse_str(str):
#   return str[::-1]
  
# str = input("Input a string: ")
# reverse = reverse_str(str)
# print(reverse)

##Bai1.4
# def is_palindrome(str):
#   if str[::-1] != str:
#     return False
#   return True
# str = input("Input a string: ")
# palindrome = is_palindrome(str)
# if palindrome == True:
#   print("This is a palindrome")
# else:
#   print("This is not a palindrome")
  
##Bai2.1
# def factorial(num):
#   if num == 0:
#     return 1
#   elif num == 1:
#     return 1
#   elif num >= 2:
#     return num * factorial(num - 1)

# num = int(input("Input a number: "))
# factorial_num = factorial(num)
# print(factorial_num)

##Bai2.2
# def sort(arr):
#   for i in range(0, len(arr)):
#     for j in range(0, len(arr)):
#       if arr[i] < arr[j]:
#         arr[i], arr[j] = arr[j], arr[i]
#   return arr

# arr = [5, 1, 8, 92, -1, 30]
# sort_arr = sort(arr)
# print(sort_arr)

## Bai2.3
# def print_fibo(num):
#   fibonacci = [1, 1]
#   a = fibonacci[0]; b = fibonacci[1]
#   for k in range(2, num + 1):
#     c = a + b
#     fibonacci.append(c)
#     a, b = b, c
#   return fibonacci

# num = int(input("Input a number: "))
# fibonacci = print_fibo(num)
# print(fibonacci)

## Bai3
import random, os, msvcrt

os.system('cls')
ch = msvcrt.getch().decode('utf-8')

rows, cols = 5, 8

player_x, player_y = random.randint(0, cols - 1), random.randint(0, rows - 1)

key_x, key_y = random.randint(0, cols - 1), random.randint(0, rows - 1)
door_x, door_y = random.randint(0, cols - 1), random.randint(0, rows - 1)

while (key_x, key_y) == (player_x, player_y):
    key_x, key_y = random.randint(0, cols - 1), random.randint(0, rows - 1)

while (door_x, door_y) == (player_x, player_y) or (door_x, door_y) == (key_x, key_y):
    door_x, door_y = random.randint(0, cols - 1), random.randint(0, rows - 1)

has_key = False

print("== THE ESCAPE GAME ==")
print("Use W A S D to move (P)layer")
print("Find (K)ey first then exit through the (D)oor")

while True:
    for i in range(rows):
        for j in range(cols):
            if (i, j) == (player_y, player_x):
                print("P", end=" ")
            elif (i, j) == (key_y, key_x):
                if has_key:
                    print(" ", end=" ")
                else:
                    print("K", end=" ")
            elif (i, j) == (door_y, door_x):
                print("D", end=" ")
            else:
                print("_", end=" ")
        print()
        
    move = input("Use W/A/S/D: ").upper()

    if move == "W" and player_y > 0:
        player_y -= 1
    elif move == "S" and player_y < rows - 1:
        player_y += 1
    elif move == "A" and player_x > 0:
        player_x -= 1
    elif move == "D" and player_x < cols - 1:
        player_x += 1

    if (player_x, player_y) == (key_x, key_y):
        has_key = True
        key_x, key_y = -1, -1

    if (player_x, player_y) == (door_x, door_y):
        if has_key:
            print("YOU WIN!")
        else:
            print("YOU LOSE! YOU HAVE TO TAKE THE KEY FIRST!")
        break

print("== THE ESCAPE GAME ==")
print("Use W A S D to move (P)layer")
print("Find (K)ey first then exit through the (D)oor")