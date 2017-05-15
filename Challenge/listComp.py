print(list(map(lambda x: x * 2, range(1, 11))))

# list comprehension

print([x * 2 for x in range(1, 11)])

print(list(filter((lambda x: x % 2), range(1, 11))))

print([x for x in range(1, 11) if x % 2])

# Generate 50 values
# Take to the power of 2
# Return multiples of 8

p = [i ** 2 for i in range(50) if i % 8 == 0]
print(p)

print([x * y for x in range(1, 3) for y in range(10, 13)])

# Generate a list of 10 values
# Multiple them by 2
# Return multiples of 8

print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
