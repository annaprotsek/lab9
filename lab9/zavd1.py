def string_to_tuple(s):
    return tuple(map(float, s.split()))

input_string = "1.2 2.3 3.4 4.5"
result = string_to_tuple(input_string)
print(result)
