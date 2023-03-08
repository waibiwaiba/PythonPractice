"""random integer"""
import random
print(random.randint(0, 10))


"""second largest. If you want smallest, max->min"""
nums = [5, 12, 54, 87, 55, 69, 23, 17]
nums.remove(max(nums))
second_largest = max(nums)
print(second_largest)


"""recursive decimal->binary"""
def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n // 2)
    print(n % 2, end="")
print("13")
dec_to_binary(13)
print("")

"""recursive reverse string print"""
def recursive_reverse_str_print(str):
    print(str[-1], end="")
    if len(str) > 1:
        recursive_reverse_str_print(str[:-1])
str1 = "abcde"
print(str1)
recursive_reverse_str_print(str1)


'''reverse str using stack'''
def reverse_stack(str):
    stack = []
    for letter in str:
        stack.append(letter)
    # stack.reverse(): reverse a list.
    while len(stack) > 0:
        print(stack.pop(), end="")
print("")
reverse_stack("abcde")
print("")


'''reverse using list.reverse()'''
str1 = "abcde"
l1 = list(str1)
print(l1)
l1.reverse()
print(l1)
for letter in l1:
    print(letter, end="")
print("")

