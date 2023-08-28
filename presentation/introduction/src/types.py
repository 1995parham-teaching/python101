print(f"{'':*<50s}\nworking with numbers:\n{'':*<50s}")

number = 10
print(f"number: {number} ({type(number)})")

number = 10.1
print(f"number: {number} ({type(number)})")

number = 1j
print(f"number * number: {(number * number).real} ({type(number)})")

number = 10 / 3
print(f"10 / 3 = {number} ({type(number)})")

number = 10 // 3
print(f"10 // 3 = {number} ({type(number)})")

print(f"{'':*<50s}\nworking with strings:\n{'':*<50s}")

string_one = "parham\n"
string_two = "پرهام\n"
print(string_one)
print(string_two)

print(f"{'':*<50s}\nworking with list, tuple and dict:\n{'':*<50s}")

my_set = {1, 2, 3, "parham"}
my_list = [1, 2, 3, "parham"]
my_tuple = (1, 2, 10, "python")

print(my_set)
print(my_list)
print(my_tuple)

my_set.add(10)
print(my_set)

print(my_list[0])
print(my_list[-1])
