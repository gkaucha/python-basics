print("Create a for loop that counts from 0 to 10, and prints odd numbers to the screen.")
for i in range(0,11):
  if i % 2 :
    print(i)


print()


print("Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.") 

x = 1
while x < 11:
  if x % 2:
    print(x)
  x += 1


print()

"""
Create a program with a for loop and a break statement. 
The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, 
and print the part before @ on one line.
"""
for ch in "gaganmagar018@gmail.com":
  if ch == "@":
    break
  print(ch, end="")


print()

"""
  Create a program with a for loop and a continue statement. 
  The program should iterate over a string of digits, replace each 0 with x, 
  and print the modified string to the screen.
 """
for digit in "0165031806510":
    if digit == "0":
      print("x", end="")
      continue
    print(digit,end="")