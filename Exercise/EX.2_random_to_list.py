# exercise Program random to list
# find the average number of the list maximum number in a list ,minimun nunber and summation of the list
import random

list = []

for i in range(10):
    num = random.randint(1, 100)  # Generate random numbers between 1 and 100
    list.append(num)
    sum =+ num
max_num = max(list)
min_num = min(list)
avg = float(sum / len(list))
print(f"List: {list}")
print(f"Maximum number: {max_num}") 
print(f"Minimum number: {min_num}")
print(f"Sum of the list: {sum}")
print(f"Average of the list: {avg:.2f}")