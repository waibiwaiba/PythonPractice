# random integer
import random
print(random.randint(0, 10))

# second largest. If you want smallest, max->min
nums = [5, 12, 54, 87, 55, 69, 23, 17]
nums.remove(max(nums))
second_largest = max(nums)
print(second_largest)

# recursive decimal->binary
def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n // 2)
    print(n % 2, end="")
num = int(input("Your decimal number: "))
dec_to_binary(num)
print(" ")
