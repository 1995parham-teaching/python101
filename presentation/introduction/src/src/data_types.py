print(f"{'':*<50s}\nworking with numbers:\n{'':*<50s}")

int_number = 10
print(f"number: {int_number} ({type(int_number)})")

float_number = 10.1
print(f"number: {float_number} ({type(float_number)})")

complex_number = 1j
print(
    f"number * number: {(complex_number * complex_number).real} ({type(complex_number)})"
)

division_result = 10 / 3
print(f"10 / 3 = {division_result} ({type(division_result)})")

floor_division_result = 10 // 3
print(f"10 // 3 = {floor_division_result} ({type(floor_division_result)})")

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
