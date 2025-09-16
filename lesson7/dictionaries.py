# Dictionaries - look very much like JS Objects
band = {"vocals": "Plant", "guitar": "Page"}

band_2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band_2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values)

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band_2.clear()
print(band_2)

del band_2

# Copy dictionaries

# band_2 = band  # creates a reference
# print("Bad copy!")
# print(band_2)
# print(band)

# band_2["drums"] = "Dave"
# print(band)

band_2 = band.copy()
band_2["drums"] = "Steve"
print("Good copy!")
print(band)
print(band_2)

# or use the dict() constructor function
band_3 = dict(band)
print("Good copy!")
print(band_3)

# NEsted dictionaries

member_1 = {"name": "Plant", "instrument": "vocals"}

member_2 = {"name": "Page", "instrument": "guitar"}

band = {"member1": member_1, "member2": member_2}
print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums_2 = set((1, 2, 3, 4))

print(nums)
print(nums_2)
print(type(nums))
print(len(nums))

# No duplicates allowed in a Set
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1,
# False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)


# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set
# with an index position or a key


# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)

# you can use update with lists,
# tuples, and dictionaries too.

# Merge two sets to crate a new set
one = {1, 2, 3}
two = {5, 6, 7}

my_new_set = one.union(two)
print(my_new_set)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)

# Use a set + dot notation to experiment,
# and reference with Python docs
# for learning methods
