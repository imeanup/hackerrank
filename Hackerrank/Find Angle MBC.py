# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

theta = math.degrees(math.atan(AB/BC))
print(f"{round(theta)}"u"\xb0")
