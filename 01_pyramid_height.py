"""
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

Write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, 
they finish their work immediately.
"""

blocks = int(input("Enter the number of blocks: "))

height = 0;
layer = 1;

while layer <= blocks:
   
    height += 1;
    blocks -= layer;
    layer += 1;

    
print("The height of the pyramid:", height)


"""

A pyramid of height N has 1 + 2 + ... + N blocks in it. This reduces toN * (N + 1) / 2. 
So you need to find the largest integer of the form (N^2 + N) / 2 that is less than or equal to your chosen number blocks. 
The quadratic is : N^2 + N - 2 * blocks = 0, 
with roots at N = floor((-1 +/- sqrt(1 + 8 * blocks)) / 2).
Since blocks is a positive integer, the negative root will never apply in this case. You can use int for floor and **0.5 for sqrt to get:
"""

# blocks = int(input("Enter number of blocks: "))
# print(f'The height of pyramid : {int(0.5 * ((8 * blocks + 1)**0.5 - 1))}')