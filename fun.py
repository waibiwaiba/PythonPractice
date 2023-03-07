# random integer
import random
print(random.randint(0, 10))

# second largest. If you want smallest, max->min
nums = [5, 12, 54, 87, 55, 69, 23, 17]
nums.remove(max(nums))
second_largest = max(nums)
print(second_largest)