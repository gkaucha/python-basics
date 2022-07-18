"""
1. take any non-negative and non-zero integer number and name it c0;
2. if it's even, evaluate a new c0 as c0 ÷ 2;
3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4. if c0 ≠ 1, skip to point 2.

The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.

Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

"""

c0 = int(input("Enter a non-negative and non-zero number: "))

steps = 0

while c0 != 1:

  if c0 % 2 == 0:
    c0 /= 2
  elif c0 % 2 == 1:
    c0 = 3*c0+1
  
  steps += 1
  print(int(c0))

print("Steps = ",steps)




