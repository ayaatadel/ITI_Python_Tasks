# Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# increased by one from start.
def generate_array(length, start):
    print ([start + i for i in range(length)])

generate_array(5, 3)




