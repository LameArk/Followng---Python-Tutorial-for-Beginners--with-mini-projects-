users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

empty_list = []

print("Dave" in empty_list)

print(users[0])
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(nums)
print(nums_copy)
print(my_nums)
my_copy.sort()
print(my_copy)

print(type(nums))

my_list = list([1, "Neil", True])
print(my_list)

# Tuples

my_tuple = tuple(("Dave", 42, True))

another_tuple = (1, 4, 2, 8, 2, 2)

print(my_tuple)
print(type(my_tuple))
print(type(another_tuple))

new_list = list(my_tuple)
new_list.append("Neil")
new_tuple = tuple(new_list)
print(new_tuple)

(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)

print(another_tuple.count(2))
