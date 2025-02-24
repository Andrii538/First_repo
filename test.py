example_1 = "1 2 3 4 5"
example_2 = "1 2 -3 4 5"
example_3 = "1 9 3 4 -5"
def higt_and_low(numbers_str: str) -> str:
    numbers = numbers_str.split()
    numbers.sort()
#    higt = numbers.pop(0)
#    low = numbers.pop(-1)
    return print(numbers.pop(0), numbers.pop(-1))
higt_and_low(example_3)
